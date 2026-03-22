#!/usr/bin/env python3
"""
md_hydrator.py

Hidrata um arquivo Markdown template, inserindo dentro de blocos de código o
conteúdo dos arquivos referenciados por nome.

Padrão esperado no Markdown (exemplos válidos):
- arquivo.py
    ```<qualquer>
    ```

- ### arquivo.html
    ```html
    (se estiver preenchido, será substituído)
    ```

Observações:
- O script indexa arquivos pelo *filename* (ex.: "main.py") no diretório atual
  e subdiretórios.
- Se houver nomes duplicados (mesmo filename em paths diferentes), ele escolhe
  deterministamente o caminho com menor "profundidade" (menor quantidade de
  partes) e, em empate, o de ordem lexicográfica.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


IGNORE_DIRS_DEFAULT = {
    ".git",
    ".hg",
    ".svn",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".tox",
    "venv",
    ".venv",
    "env",
    ".env",
    "node_modules",
    "dist",
    "build",
}


LANG_BY_EXT = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".tsx": "tsx",
    ".jsx": "jsx",
    ".json": "json",
    ".html": "html",
    ".htm": "html",
    ".css": "css",
    ".scss": "scss",
    ".md": "markdown",
    ".yml": "yaml",
    ".yaml": "yaml",
    ".toml": "toml",
    ".ini": "ini",
    ".cfg": "ini",
    ".xml": "xml",
    ".sh": "bash",
    ".bash": "bash",
    ".zsh": "zsh",
    ".ps1": "powershell",
    ".sql": "sql",
    ".java": "java",
    ".kt": "kotlin",
    ".c": "c",
    ".h": "c",
    ".cpp": "cpp",
    ".hpp": "cpp",
    ".go": "go",
    ".rs": "rust",
    ".rb": "ruby",
    ".php": "php",
    ".dockerfile": "dockerfile",
}


FENCE_RE = re.compile(r"^(?P<indent>\s*)```")  # abertura/fechamento


@dataclass
class HydrationStats:
    """Estatísticas do processo de hidratação."""
    blocks_found: int = 0
    blocks_hydrated: int = 0
    files_missing: int = 0
    files_ambiguous: int = 0
    read_errors: int = 0


def build_file_index(base_dir: Path, ignore_dirs: Iterable[str]) -> Dict[str, List[Path]]:
    """Cria um índice de arquivos por nome, varrendo recursivamente.

    Args:
        base_dir: Diretório base para varredura (normalmente Path(".")).
        ignore_dirs: Nomes de diretórios a ignorar (match por nome, não por path).

    Returns:
        Dicionário {filename: [caminhos...]} com caminhos relativos a base_dir.
    """
    ignore_set = set(ignore_dirs)
    index: Dict[str, List[Path]] = {}

    # os.walk permite podar diretórios (mais eficiente do que rglob + filtros).
    for root, dirs, files in os.walk(base_dir):
        root_path = Path(root)

        # poda diretórios ignorados (in-place)
        dirs[:] = [d for d in dirs if d not in ignore_set]

        for fn in files:
            p = root_path / fn
            if not p.is_file():
                continue
            rel = p.relative_to(base_dir)
            index.setdefault(fn, []).append(rel)

    # ordena listas para escolha determinística
    for fn, paths in index.items():
        paths.sort(key=lambda x: (len(x.parts), str(x).lower()))

    return index


def guess_language_from_filename(filename: str) -> str:
    """Deduz a linguagem do bloco Markdown a partir da extensão do arquivo."""
    lower = filename.lower()
    suffix = Path(lower).suffix

    # caso especial: "Dockerfile" (sem extensão)
    if lower == "dockerfile":
        return "dockerfile"

    if suffix in LANG_BY_EXT:
        return LANG_BY_EXT[suffix]

    # fallback: usa extensão sem ponto, quando existir
    return suffix.lstrip(".")


def extract_filename_candidate(line: str) -> Optional[str]:
    """Tenta extrair um 'nome de arquivo' de uma linha Markdown.

    Aceita padrões comuns como:
    - "arquivo.py"
    - "- arquivo.py"
    - "### arquivo.py"
    - "`arquivo.py`"

    Regras conservadoras:
    - Deve ser um token único (sem espaços internos).
    - Deve conter ao menos um ponto (extensão), OU ser "Dockerfile".

    Args:
        line: Linha original do Markdown.

    Returns:
        O filename (ex.: "main.py") ou None se não parecer um filename.
    """
    s = line.strip()

    # remove marcadores comuns do começo
    s = re.sub(r"^[-*+]\s+", "", s)     # listas
    s = re.sub(r"^#{1,6}\s+", "", s)    # headings
    s = s.strip()

    # remove backticks simples envolvendo o token
    if len(s) >= 2 and s[0] == "`" and s[-1] == "`":
        s = s[1:-1].strip()

    if not s or " " in s or "\t" in s:
        return None

    # limpa pontuação final comum em textos (ex: "arquivo.py:" ou "arquivo.py,")
    s = s.rstrip(":,;.")

    if not s:
        return None

    if s.lower() == "dockerfile":
        return "Dockerfile"

    # precisa ter extensão básica
    if "." not in s:
        return None

    # evita capturar coisas tipo "www.exemplo.com" (heurística simples)
    if s.count(".") >= 3 and (s.endswith(".com") or s.endswith(".org") or s.endswith(".net")):
        return None

    return s


def find_fence_bounds(lines: List[str], open_idx: int) -> Optional[int]:
    """Encontra o índice do fechamento ``` correspondente, a partir da abertura.

    Args:
        lines: Linhas do arquivo Markdown.
        open_idx: Índice da linha de abertura do fence.

    Returns:
        Índice da linha de fechamento ou None se não encontrar.
    """
    for k in range(open_idx + 1, len(lines)):
        if FENCE_RE.match(lines[k]):
            return k
    return None


def choose_best_path(paths: List[Path]) -> Path:
    """Escolhe deterministamente o melhor path dentre candidatos (já ordenados)."""
    return paths[0]


def read_text_file(path: Path) -> str:
    """Lê arquivo texto como UTF-8, substituindo caracteres inválidos.

    Args:
        path: Caminho do arquivo a ser lido.

    Returns:
        Conteúdo do arquivo (string).
    """
    return path.read_text(encoding="utf-8", errors="replace")


def hydrate_markdown(md_path: Path, file_index: Dict[str, List[Path]]) -> Tuple[str, HydrationStats]:
    """Hidrata o Markdown substituindo blocos de código pelo conteúdo de arquivos.

    Estratégia:
    - Varre linha a linha.
    - Quando encontra uma linha que parece ser um filename, procura (logo abaixo)
      uma linha de abertura de fence ``` (pulando linhas em branco, até 3 linhas).
    - Ao achar, localiza o fechamento e substitui o conteúdo interno pelo texto
      do arquivo encontrado.
    - Também ajusta a linguagem do fence (```python, ```html, etc.) a partir da extensão.

    Args:
        md_path: Caminho do .md alvo.
        file_index: Índice {filename: [paths...]} baseado no diretório atual.

    Returns:
        (texto_novo, stats)
    """
    stats = HydrationStats()
    original = md_path.read_text(encoding="utf-8", errors="replace")
    lines = original.splitlines(keepends=True)

    i = 0
    while i < len(lines):
        candidate = extract_filename_candidate(lines[i])
        if not candidate:
            i += 1
            continue

        # procura fence logo abaixo (pulando até 3 linhas em branco)
        j = i + 1
        blanks_skipped = 0
        while j < len(lines) and lines[j].strip() == "" and blanks_skipped < 3:
            j += 1
            blanks_skipped += 1

        m = FENCE_RE.match(lines[j]) if j < len(lines) else None
        if not m:
            i += 1
            continue

        open_idx = j
        close_idx = find_fence_bounds(lines, open_idx)
        if close_idx is None:
            # fence malformado; não mexe
            i += 1
            continue

        stats.blocks_found += 1

        # resolve arquivo no índice
        paths = file_index.get(candidate)
        if not paths:
            stats.files_missing += 1
            i = close_idx + 1
            continue

        if len(paths) > 1:
            stats.files_ambiguous += 1

        rel_path = choose_best_path(paths)
        disk_path = (Path(".") / rel_path).resolve()

        try:
            content = read_text_file(disk_path)
        except (FileNotFoundError, PermissionError, OSError):
            stats.read_errors += 1
            i = close_idx + 1
            continue

        # normaliza para terminar com newline (fica mais bonito e estável)
        if content and not content.endswith("\n"):
            content += "\n"

        # define linguagem do fence
        indent = m.group("indent")
        lang = guess_language_from_filename(candidate)
        fence_open = f"{indent}```{lang}\n" if lang else f"{indent}```\n"

        # substitui: linha de abertura + miolo + linha de fechamento
        new_inner_lines = content.splitlines(keepends=True) if content else []
        lines[open_idx] = fence_open
        lines[open_idx + 1:close_idx] = new_inner_lines

        # após substituir, precisamos reposicionar i corretamente
        # close_idx mudou? Recalcula: novo fechamento está em open_idx + 1 + len(inner)
        close_idx = open_idx + 1 + len(new_inner_lines)
        # garantir que a linha de fechamento exista (ela está onde era antes, mas a slice preserva)
        # Como fizemos slice assignment, a linha que era o fechamento foi deslocada automaticamente.
        # A maneira robusta: procurar o próximo fence a partir de open_idx+1.
        next_close = find_fence_bounds(lines, open_idx)
        if next_close is not None:
            i = next_close + 1
        else:
            i = open_idx + 1

        stats.blocks_hydrated += 1

    return "".join(lines), stats


def atomic_write(path: Path, text: str) -> None:
    """Escreve arquivo de forma atômica (best-effort) usando arquivo temporário.

    Args:
        path: Caminho de destino.
        text: Conteúdo a ser escrito.
    """
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", errors="replace")
    tmp.replace(path)


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    """Parse de argumentos CLI."""
    parser = argparse.ArgumentParser(
        description="Hidrata um template Markdown inserindo conteúdo de arquivos em blocos ```."
    )
    parser.add_argument(
        "markdown",
        type=str,
        help="Caminho do arquivo .md template (ex: exemplo.md)",
    )
    parser.add_argument(
        "--root",
        type=str,
        default=".",
        help="Diretório raiz para varredura (default: diretório atual).",
    )
    parser.add_argument(
        "--ignore",
        type=str,
        default=",".join(sorted(IGNORE_DIRS_DEFAULT)),
        help="Lista de diretórios ignorados, separados por vírgula.",
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Cria um backup .bak do Markdown antes de sobrescrever.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    """Ponto de entrada do script."""
    args = parse_args(argv)

    md_path = Path(args.markdown)
    if not md_path.exists():
        print(f"[erro] Markdown não encontrado: {md_path}", file=sys.stderr)
        return 2
    if not md_path.is_file():
        print(f"[erro] Não é arquivo: {md_path}", file=sys.stderr)
        return 2

    root = Path(args.root)
    if not root.exists() or not root.is_dir():
        print(f"[erro] Root inválido: {root}", file=sys.stderr)
        return 2

    ignore_dirs = [x.strip() for x in args.ignore.split(",") if x.strip()]
    file_index = build_file_index(root, ignore_dirs)

    # O índice foi construído relativo ao root; para este script, assumimos execução no root.
    # Se root != ".", ajusta CWD lógico mudando temporariamente o diretório de execução.
    old_cwd = Path.cwd()
    try:
        os.chdir(root)
        new_text, stats = hydrate_markdown(md_path.resolve().relative_to(root.resolve()), file_index)
    finally:
        os.chdir(old_cwd)

    # Se nada mudou, não escreve (idempotência + evita tocar mtime).
    old_text = md_path.read_text(encoding="utf-8", errors="replace")
    if new_text == old_text:
        print("[ok] Nenhuma alteração necessária.")
        print(
            f"[info] blocos_encontrados={stats.blocks_found} "
            f"hidratados={stats.blocks_hydrated} "
            f"ausentes={stats.files_missing} "
            f"ambiguos={stats.files_ambiguous} "
            f"erros_leitura={stats.read_errors}"
        )
        return 0

    if args.backup:
        bak = md_path.with_suffix(md_path.suffix + ".bak")
        bak.write_text(old_text, encoding="utf-8", errors="replace")

    atomic_write(md_path, new_text)

    print("[ok] Markdown hidratado com sucesso.")
    print(
        f"[info] blocos_encontrados={stats.blocks_found} "
        f"hidratados={stats.blocks_hydrated} "
        f"ausentes={stats.files_missing} "
        f"ambiguos={stats.files_ambiguous} "
        f"erros_leitura={stats.read_errors}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
