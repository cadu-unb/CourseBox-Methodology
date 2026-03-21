# lib.md - Biblioteca do Scaffold

Este arquivo centraliza ferramentas, arquivos de configuração e templates de README
utilizados pelo `scaffold.py` para montar e documentar projetos Python.

## 📌 Índice

- [lib.md - Biblioteca do Scaffold](#libmd---biblioteca-do-scaffold)
  - [📌 Índice](#-índice)
  - [Formato dos blocos](#formato-dos-blocos)
  - [Ferramentas (TOOL)](#ferramentas-tool)
- [Coding Conventions](#coding-conventions)
  - [📌 Índice](#-índice-1)
  - [Princípios gerais](#princípios-gerais)
  - [Nomenclatura de diretórios](#nomenclatura-de-diretórios)
      - [✔ Bom](#-bom)
      - [❌ Ruim](#-ruim)
  - [Nomenclatura de arquivos e módulos](#nomenclatura-de-arquivos-e-módulos)
      - [✔ Bom](#-bom-1)
      - [❌ Ruim](#-ruim-1)
  - [Classes](#classes)
      - [✔ Bom](#-bom-2)
      - [❌ Ruim](#-ruim-2)
  - [Funções](#funções)
      - [✔ Bom](#-bom-3)
      - [❌ Ruim](#-ruim-3)
  - [Variáveis](#variáveis)
      - [✔ Bom](#-bom-4)
      - [❌ Ruim](#-ruim-4)
  - [Constantes](#constantes)
      - [✔ Bom](#-bom-5)
      - [❌ Ruim](#-ruim-5)
  - [Modelos de tipos (Python 3)](#modelos-de-tipos-python-3)
      - [Exemplo básico](#exemplo-básico)
    - [Tipos comuns](#tipos-comuns)
      - [Listas](#listas)
      - [Dicionários](#dicionários)
      - [Opcional](#opcional)
      - [União de tipos](#união-de-tipos)
      - [Estruturas de dados com `dataclass`](#estruturas-de-dados-com-dataclass)
  - [Docstrings (padrão Doxygen)](#docstrings-padrão-doxygen)
    - [Exemplo correto](#exemplo-correto)
    - [Exemplo incorreto](#exemplo-incorreto)
  - [Imports](#imports)
  - [Padrões para pipelines de dados](#padrões-para-pipelines-de-dados)
      - [Pipeline deve:](#pipeline-deve)
      - [Estrutura recomendada](#estrutura-recomendada)
      - [Exemplo de pipeline](#exemplo-de-pipeline)
  - [Boas práticas gerais](#boas-práticas-gerais)
  - [Objetivo destas convenções](#objetivo-destas-convenções)
  - [Templates de README (README)](#templates-de-readme-readme)
- [{nome\_projeto}](#nome_projeto)
  - [📌 Índice](#-índice-2)
  - [🛠️ Instalação](#️-instalação)
    - [1. Instalando o `uv`](#1-instalando-o-uv)
    - [2. Doxygen (Opcional)](#2-doxygen-opcional)
  - [🚀 Setup](#-setup)
- [Ferramentas de Desenvolvimento](#ferramentas-de-desenvolvimento)
  - [📌 Objetivo](#-objetivo)
  - [📂 Conteúdo](#-conteúdo)
  - [📏 Regras](#-regras)
  - [Comandos Úteis](#comandos-úteis)
    - [Na raiz do projeto](#na-raiz-do-projeto)
      - [Novos Pacotes](#novos-pacotes)
      - [Tree](#tree)
      - [Scaffold](#scaffold)

## Formato dos blocos

Existem três tipos de bloco reconhecidos pelo parser:

**TOOL** — arquivo `.py` copiado para `2_devtools/py/`:
```
    <!-- TOOL: arquivo.py | nome_pacote | Descrição curta -->
    <!-- END -->
```

**FILE** — arquivo de configuração copiado para o destino definido em `scaffold.py`:
```
    <!-- FILE: nome_do_arquivo -->
    <!-- END -->
```

**README** — template de README com placeholders dinâmicos:
```
    <!-- README: identificador -->
    <!-- END -->
```

---

## Ferramentas (TOOL)

<!-- TOOL: file_tree.py | file-tree | Gera a árvore de arquivos do projeto com filtros configuráveis -->
```py
import os

DEFAULT_CONFIG: dict = {
    "ignored_dirs":       ["__pycache__", ".git", "node_modules", ".vscode"],
    "visible_extensions": [],
    "ignored_extensions": [],
    "visible_files":      [],
}


def normalize_extensions(extension_list: list[str]) -> list[str]:
    """!
    @brief Normaliza extensões para o formato '.ext'.
    @param extension_list Lista de extensões.
    @return Lista normalizada.
    """
    if not extension_list:
        return []
    normalized = []
    for ext in extension_list:
        ext = ext.lower().strip()
        if ext and not ext.startswith("."):
            ext = f".{ext}"
        normalized.append(ext)
    return normalized


def should_include_item(item_name: str, relative_path: str, is_dir: bool, config: dict) -> bool:
    """!
    @brief Decide se um item deve aparecer na árvore.
    @param item_name Nome do item.
    @param relative_path Caminho relativo ao root.
    @param is_dir True se for diretório.
    @param config Dicionário de filtros.
    @return True se o item deve ser incluído.
    """
    item_name_lower = item_name.lower()

    if is_dir:
        if (
            item_name_lower.startswith(".")
            or item_name_lower in config["ignored_dirs"]
            or relative_path in config["ignored_dirs"]
        ):
            return False
        return True

    extension = os.path.splitext(item_name_lower)[1]

    if extension in config["ignored_extensions"]:
        return False
    if item_name in config["visible_files"] or relative_path in config["visible_files"]:
        return True
    if not config["visible_extensions"]:
        return True
    return extension in config["visible_extensions"]


def generate_file_tree(
    base_path: str,
    current_path: str,
    prefix: str = "",
    config: dict = None,
) -> tuple[list[str], list[str], dict]:
    """!
    @brief Gera recursivamente a árvore visual e lista de caminhos.
    @param base_path Raiz do projeto.
    @param current_path Diretório atual.
    @param prefix Indentação atual.
    @param config Filtros (usa DEFAULT_CONFIG se None).
    @return Tupla (linhas, caminhos, estatísticas).
    """
    if config is None:
        config = DEFAULT_CONFIG

    lines      = []
    file_paths = []
    stats      = {"files": 0, "dirs": 0}

    try:
        items = os.listdir(current_path)
    except PermissionError:
        return [f"{prefix} [Acesso Negado]"], [], stats
    except FileNotFoundError:
        return [f"{prefix} [Diretório não encontrado]"], [], stats

    filtered_items = []
    for item in items:
        full_path = os.path.join(current_path, item)
        rel_path  = os.path.relpath(full_path, base_path).replace("\\", "/")
        is_directory = os.path.isdir(full_path)
        if should_include_item(item, rel_path, is_directory, config):
            filtered_items.append((item, full_path, rel_path, is_directory))

    filtered_items.sort(key=lambda x: (not x[3], x[0].lower()))

    for i, (name, full_path, rel_path, is_directory) in enumerate(filtered_items):
        is_last   = i == len(filtered_items) - 1
        connector = "└── " if is_last else "├── "
        lines.append(f"{prefix}{connector}{name}")

        if is_directory:
            stats["dirs"] += 1
            new_prefix = prefix + ("    " if is_last else "│   ")
            sub_lines, sub_paths, sub_stats = generate_file_tree(
                base_path, full_path, new_prefix, config
            )
            lines.extend(sub_lines)
            file_paths.extend(sub_paths)
            stats["files"] += sub_stats["files"]
            stats["dirs"]  += sub_stats["dirs"]
        else:
            stats["files"] += 1
            file_paths.append(rel_path)

    return lines, file_paths, stats


def save_output(filename: str, content: list[str]) -> bool:
    """!
    @brief Salva conteúdo em arquivo de texto.
    @param filename Destino.
    @param content Linhas a salvar.
    @return True se bem-sucedido.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(content))
        return True
    except Exception as e:
        print(f"Erro ao salvar {filename}: {e}")
        return False


def main():
    target_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

    config = {
        "ignored_dirs":       ["__pycache__", ".git", "node_modules", ".vscode"],
        "visible_extensions":  normalize_extensions([]),
        "ignored_extensions":  normalize_extensions(["log", "tmp", "exe", "txt"]),
        "visible_files":       [],
    }

    print(f"\nAnalisando: {os.path.abspath(target_directory)}")

    tree_body, path_list, summary = generate_file_tree(
        target_directory, target_directory, config=config
    )
    final_tree = ["Projeto/"] + tree_body

    success_tree  = save_output("tree_focada.txt", final_tree)
    success_paths = save_output("caminhos.txt",    path_list)

    print("\n" + "="*40)
    if success_tree and success_paths:
        print(f"Arquivos gerados:")
        print(f"  tree_focada.txt  ({len(final_tree)} linhas)")
        print(f"  caminhos.txt     ({len(path_list)} arquivos)")
        print(f"  Pastas: {summary['dirs']} | Arquivos: {summary['files']}")
    else:
        print("Houve problemas ao salvar os arquivos de saída.")
    print("="*40 + "\n")


if __name__ == "__main__":
    main()
```
<!-- END -->

<!-- TOOL: gen_docs.py | gen-docs | Invoca o Doxygen com caminho absoluto a partir do diretório correto -->
```py
import subprocess
from pathlib import Path


def generate_docs() -> None:
    """!
    @brief Localiza o Doxyfile via caminho absoluto e invoca o Doxygen.
    @details Resolve o caminho independentemente de onde o script é executado.
    """
    script_path  = Path(__file__).resolve()
    project_root = script_path.parents[2]
    doxyfile     = project_root / "0_docs" / "2_api" / "doxygen" / "Doxyfile"
    workdir      = doxyfile.parent

    if not doxyfile.exists():
        print(f"[!] Doxyfile não encontrado em: {doxyfile}")
        return

    print(f"[*] Gerando documentação a partir de: {workdir}")

    try:
        result = subprocess.run(
            ["doxygen", str(doxyfile)],
            cwd=str(workdir),
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("[V] Documentação gerada com sucesso.")
            print(f"[i] Saída em: {workdir / 'html' / 'index.html'}")
        else:
            print("[!] Doxygen reportou erros:")
            print(result.stderr)
    except FileNotFoundError:
        print("[!] Doxygen não encontrado. Instale em: https://www.doxygen.nl/download.html")


if __name__ == "__main__":
    generate_docs()
```
<!-- END -->

<!-- TOOL: md_hydrator.py | md_hydrator | Completa arquivos .md para anexos -->
```
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
```

<!-- END -->

<!-- FILE: .gitignore -->
```
# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Waste
tree_focada.txt
caminhos.txt
0_docs/doxygen/html/

# Folders
## Virtual Environments
.venv

## VSCODE
.vscode

## Project
3_data/
4_test/
```
<!-- END -->

<!-- FILE: conftest.py -->
```py
import sys
from pathlib import Path

# Adiciona 1_src ao sys.path para que pacotes dentro dele sejam importáveis
# independentemente do prefixo numérico do diretório pai.
sys.path.insert(0, str(Path(__file__).resolve().parent / "1_src"))
```
<!-- END -->

<!-- FILE: Doxyfile -->
```
# Nome do projeto
PROJECT_NAME = "{project_name}"

# Onde está o código
INPUT = ../../1_src

# Extensões Python
FILE_PATTERNS = *.py

# Habilitar Python
OPTIMIZE_OUTPUT_JAVA = NO
OPTIMIZE_OUTPUT_FOR_C = NO
EXTENSION_MAPPING = py=Python

# Extrair tudo
EXTRACT_ALL = YES

# Docstrings como documentação
JAVADOC_AUTOBRIEF = YES

# Saída
OUTPUT_DIRECTORY = .
GENERATE_HTML = YES
GENERATE_LATEX = NO
```
<!-- END -->

<!-- FILE: conventions.md -->
```md
# Coding Conventions

Este documento define as **convenções de código utilizadas neste projeto**.
As regras seguem os princípios da **PEP 8**, porém em uma versão **simplificada, prática e consistente**, adequada para projetos de pesquisa, automação e pipelines de dados em Python.

O objetivo é garantir:

* consistência no código
* facilidade de leitura
* manutenção a longo prazo
* colaboração entre desenvolvedores

## 📌 Índice

- [Coding Conventions](#coding-conventions)
  - [📌 Índice](#-índice)
  - [Princípios gerais](#princípios-gerais)
  - [Nomenclatura de diretórios](#nomenclatura-de-diretórios)
      - [✔ Bom](#-bom)
      - [❌ Ruim](#-ruim)
  - [Nomenclatura de arquivos e módulos](#nomenclatura-de-arquivos-e-módulos)
      - [✔ Bom](#-bom-1)
      - [❌ Ruim](#-ruim-1)
  - [Classes](#classes)
      - [✔ Bom](#-bom-2)
      - [❌ Ruim](#-ruim-2)
  - [Funções](#funções)
      - [✔ Bom](#-bom-3)
      - [❌ Ruim](#-ruim-3)
  - [Variáveis](#variáveis)
      - [✔ Bom](#-bom-4)
      - [❌ Ruim](#-ruim-4)
  - [Constantes](#constantes)
      - [✔ Bom](#-bom-5)
      - [❌ Ruim](#-ruim-5)
  - [Modelos de tipos (Python 3)](#modelos-de-tipos-python-3)
      - [Exemplo básico](#exemplo-básico)
    - [Tipos comuns](#tipos-comuns)
      - [Listas](#listas)
      - [Dicionários](#dicionários)
      - [Opcional](#opcional)
      - [União de tipos](#união-de-tipos)
      - [Estruturas de dados com `dataclass`](#estruturas-de-dados-com-dataclass)
  - [Docstrings (padrão Doxygen)](#docstrings-padrão-doxygen)
    - [Exemplo correto](#exemplo-correto)
    - [Exemplo incorreto](#exemplo-incorreto)
  - [Imports](#imports)
  - [Padrões para pipelines de dados](#padrões-para-pipelines-de-dados)
      - [Pipeline deve:](#pipeline-deve)
      - [Estrutura recomendada](#estrutura-recomendada)
      - [Exemplo de pipeline](#exemplo-de-pipeline)
  - [Boas práticas gerais](#boas-práticas-gerais)
  - [Objetivo destas convenções](#objetivo-destas-convenções)

## Princípios gerais

As seguintes regras devem guiar todo o desenvolvimento:

* **clareza é mais importante que brevidade**
* **consistência é mais importante que preferência pessoal**
* código deve ser **autoexplicativo**
* evitar abreviações desnecessárias
* manter funções pequenas e focadas

## Nomenclatura de diretórios

Diretórios devem utilizar **snake_case**.

Formato:

"""
snake_case
"""

#### ✔ Bom

"""
services
data_processing
video_pipeline
"""

#### ❌ Ruim

"""
VideoProcessing
video-processing
VideoPipeline
"""

## Nomenclatura de arquivos e módulos

Arquivos Python também devem utilizar **snake_case**.

Formato:

"""
snake_case.py
"""

#### ✔ Bom

"""
video_to_text.py
transcription_service.py
file_tree.py
"""

#### ❌ Ruim

"""
VideoToText.py
video-to-text.py
FileTree.py
"""

Evitar:

* nomes genéricos (`utils.py`, `helpers.py`)
* nomes muito longos
* abreviações não padronizadas

## Classes

Classes devem utilizar **PascalCase**.

Formato:

"""

PascalCase
"""

#### ✔ Bom

"""python
class Transcript:
    pass

class VideoMetadata:
    pass
"""

#### ❌ Ruim

"""python
class transcript:
    pass

class video_metadata:
    pass
"""

## Funções

Funções devem usar **snake_case**.

Formato:

"""
snake_case()
"""

#### ✔ Bom

"""python
def transcribe_video(video_path):
    pass


def clean_transcript(text):
    pass
"""

#### ❌ Ruim

"""python
def TranscribeVideo():
    pass


def cleanTranscript():
    pass
"""

## Variáveis

Variáveis também usam **snake_case**.

#### ✔ Bom

"""python
video_path = "lecture.mp4"
transcript_text = ""
video_duration = 3600
"""

#### ❌ Ruim

"""python
videoPath = "lecture.mp4"
VideoPath = "lecture.mp4"
v = "lecture.mp4"
"""

Evitar variáveis de **uma letra**, exceto em loops simples:

"""python
for i in range(10):
    pass
"""

## Constantes

Constantes devem usar **UPPER_CASE**.

#### ✔ Bom

"""python
MAX_VIDEO_DURATION = 7200
DEFAULT_LANGUAGE = "pt"
"""

#### ❌ Ruim

"""python
maxVideoDuration = 7200
defaultLanguage = "pt"
"""

## Modelos de tipos (Python 3)

O projeto deve utilizar **type hints modernos** do Python 3.

Sempre que possível, funções devem declarar tipos de entrada e saída.

#### Exemplo básico

"""python
def clean_text(text: str) -> str:
    return text.strip()
"""

### Tipos comuns

#### Listas

"""python
def process_videos(videos: list[str]) -> list[str]:
    pass
"""

#### Dicionários

"""python
def load_metadata() -> dict[str, str]:
    pass
"""

#### Opcional

"""python
from typing import Optional

def load_transcript(path: str) -> Optional[str]:
    pass
"""

#### União de tipos

Python 3.10+

"""python
def parse_input(data: str | bytes) -> str:
    pass
"""

#### Estruturas de dados com `dataclass`

Recomendado para modelos simples.

"""python
from dataclasses import dataclass

@dataclass
class Transcript:
    text: str
    language: str
"""

## Docstrings (padrão Doxygen)

Todas as funções públicas devem possuir **docstrings no padrão Doxygen**.

Formato básico:

"""
"""
Descrição da função.

@param parametro descrição
@return descrição do retorno
"""
"""

### Exemplo correto

"""python
def transcribe_video(video_path: str) -> str:
    """
    Transcreve o áudio de um vídeo.

    @param video_path Caminho do arquivo de vídeo
    @return Texto transcrito
    """
"""

### Exemplo incorreto

"""python
def transcribe_video(video_path):
    # faz a transcrição
"""

## Imports

Imports devem seguir esta ordem:

1. biblioteca padrão do Python
2. bibliotecas externas
3. módulos do projeto

Exemplo:

"""python
import os
import pathlib

import numpy as np

from arctel.services.transcription_service import transcribe
"""

Evitar:

"""python
from module import *
"""

## Padrões para pipelines de dados

Pipelines devem seguir alguns princípios estruturais.

#### Pipeline deve:

* orquestrar serviços
* conectar etapas de processamento
* evitar lógica pesada

#### Estrutura recomendada

"""
pipeline/
├── video_to_text.py
├── generate_material.py
"""

#### Exemplo de pipeline

"""python
from arctel.services.transcription_service import transcribe
from arctel.services.text_cleaning_service import clean_text


def video_to_text(video_path: str) -> str:
    """
    Pipeline de transcrição de vídeo.

    @param video_path Caminho do vídeo
    @return Texto limpo da transcrição
    """

    transcript = transcribe(video_path)
    clean = clean_text(transcript)

    return clean
"""

## Boas práticas gerais

Evitar:

* funções muito longas
* duplicação de código
* dependências desnecessárias
* lógica complexa em pipelines

Preferir:

* funções pequenas
* código explícito
* nomes claros
* separação de responsabilidades

## Objetivo destas convenções

Estas convenções existem para:

* padronizar o código do projeto
* facilitar leitura e revisão
* melhorar manutenção
* permitir crescimento sustentável do sistema
* tornar o projeto mais profissional e colaborativo
"""
<!-- END -->

---

## Templates de README (README)

<!-- README: raiz -->
"""md
# {nome_projeto}

<!-- Descrição do projeto -->

## 📌 Índice

- [{nome_projeto}](#{nome_projeto_slug})

## 🛠️ Instalação

Este projeto utiliza o **[uv](https://docs.astral.sh/uv/)** como gerenciador de pacotes.

### 1. Instalando o `uv`

No Windows (PowerShell):

"""powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
"""

### 2. Doxygen (Opcional)

Página de referência: [doxygen.nl](https://www.doxygen.nl/download.html)

## 🚀 Setup

No terminal do VSCode, dentro do projeto:

"""terminal
uv run
"""
"""

<!-- END -->

<!-- README: 2_devtools/README.md -->
"""md
# Ferramentas de Desenvolvimento

## 📌 Objetivo

Scripts auxiliares utilizados durante o desenvolvimento.

## 📂 Conteúdo

{lista_ferramentas}

## 📏 Regras

Esses scripts não fazem parte do sistema principal.
"""

<!-- END -->

<!-- README: 2_devtools/comandos -->
"""md
## Comandos Úteis

### Na raiz do projeto

#### Novos Pacotes

Para adicionar pacotes à estrutura do projeto:

"""cmd
uv add {nome_do_pacote}
"""

#### Tree

Para criar uma árvore de arquivos:

"""cmd
uv run python 2_devtools/py/file_tree.py
"""

#### Scaffold

Para criar a estrutura de um novo projeto ou verificar a integridade da atual:

"""cmd
uv run python 2_devtools/py/scaffold.py
"""
"""
<!-- END -->
