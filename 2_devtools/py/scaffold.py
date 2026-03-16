import os
import re
import sys
import argparse
import importlib.util
from pathlib import Path

# --- Parser de lib.md ---

# Substitua load_lib integralmente por esta versão

def _extract_fenced_content(block: str) -> str:
    """!
    @brief Remove a primeira e última linha de um bloco (os delimitadores de cerca).
    @param block Texto completo entre o comentário de abertura e END.
    @return Conteúdo sem os delimitadores.
    """
    lines = block.split("\n")
    # Remove linhas vazias das pontas, depois remove a linha do fence
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    if lines:
        lines.pop(0)   # remove primeira linha: ```md / """md / ``` etc.
    if lines:
        lines.pop(-1)  # remove última linha:  ``` / """
    return "\n".join(lines)


def load_lib(lib_path: Path) -> dict:
    """!
    @brief Lê lib.md e extrai blocos TOOL, FILE e README.
    @param lib_path Caminho para lib.md.
    @return Dicionário com chaves 'tools', 'files', 'readmes' e 'tool_meta'.
    """
    if not lib_path.exists():
        print(f"[!] lib.md não encontrado em: {lib_path}")
        return {"tools": {}, "files": {}, "readmes": {}, "tool_meta": {}}

    raw = lib_path.read_text(encoding="utf-8")

    # TOOL: delimitador sempre ```, nunca """ (evita conflito com docstrings internas)
    tool_pattern = re.compile(
        r"<!--\s*TOOL:\s*(?P<name>[\w\.]+)\s*\|\s*(?P<pkg>[\w\-]+)\s*\|\s*(?P<desc>[^>]+?)\s*-->"
        r".*?```(?:python|py)\n(?P<code>.*?)```"
        r".*?<!--\s*END\s*-->",
        re.DOTALL,
    )

    # FILE e README: captura tudo até <!-- END -->, sem depender do delimitador de fechamento
    file_pattern = re.compile(
        r"<!--\s*FILE:\s*(?P<name>[\w\.\/\-]+)\s*-->"
        r"(?P<block>.*?)"
        r"<!--\s*END\s*-->",
        re.DOTALL,
    )
    readme_pattern = re.compile(
        r"<!--\s*README:\s*(?P<name>[\w\.\/\-]+)\s*-->"
        r"(?P<block>.*?)"
        r"<!--\s*END\s*-->",
        re.DOTALL,
    )

    tools     = {}
    tool_meta = {}
    files     = {}
    readmes   = {}

    for m in tool_pattern.finditer(raw):
        tools[m.group("name")]     = m.group("code")
        tool_meta[m.group("name")] = {
            "pkg":  m.group("pkg"),
            "desc": m.group("desc").strip(),
        }

    for m in file_pattern.finditer(raw):
        content = _extract_fenced_content(m.group("block"))
        files[m.group("name")] = _restore_fences(content)

    for m in readme_pattern.finditer(raw):
        content = _restore_fences(m.group("block"))
        readmes[m.group("name")] = _extract_fenced_content(content)

    return {"tools": tools, "files": files, "readmes": readmes, "tool_meta": tool_meta}

def _restore_fences(content: str) -> str:
    """!
    @brief Converte aspas triplas de volta para crases triplas no conteúdo extraído.
    @param content Texto extraído do bloco em lib.md.
    @return Texto com delimitadores de código restaurados.
    """
    return content.replace('"""', "```")

# --- Funções de Apoio ---

def create_file(file_path: Path, content: str = "") -> None:
    """!
    @brief Cria um arquivo e escreve o conteúdo fornecido.
    @param file_path Caminho completo do arquivo.
    @param content Conteúdo em string.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def create_readme(file_path: Path) -> None:
    """!
    @brief Gera um README.md básico com placeholder.
    @param file_path Local do README.
    """
    header = f"# Diretório: {file_path.parent.name}\n\nConteúdo a preencher."
    create_file(file_path, header)


def slugify(name: str) -> str:
    """!
    @brief Converte nome do projeto em slug para âncoras markdown.
    @param name Nome do projeto.
    @return String em lowercase com hífens.
    """
    return name.lower().replace(" ", "-").replace("_", "-")


def build_devtools_readme(template: str, tool_meta: dict, commands_block: str) -> str:
    """!
    @brief Popula o template do README de 2_devtools com metadados das ferramentas.
    @param template String do template com placeholder {lista_ferramentas}.
    @param tool_meta Dicionário com pkg e desc de cada ferramenta.
    @param commands_block Bloco de comandos úteis extraído de lib.md.
    @return README completo como string.
    """
    lista  = "\n".join(
        f"- **{meta['pkg']}** — {meta['desc']}"
        for meta in tool_meta.values()
    )
    result = template.replace("{lista_ferramentas}", lista)
    result = result.rstrip() + "\n\n" + commands_block
    return result


def build_root_readme(template: str, nome_proj: str) -> str:
    """!
    @brief Popula o template do README raiz com nome e slug do projeto.
    @param template String do template.
    @param nome_proj Nome do projeto.
    @return README completo como string.
    """
    return (
        template
        .replace("{nome_projeto}",      nome_proj)
        .replace("{nome_projeto_slug}", slugify(nome_proj))
    )


# --- Auditoria ---

def audit_project(root_path: Path) -> None:
    """!
    @brief Verifica a integridade da estrutura do projeto.
    @param root_path Caminho raiz do projeto.
    """
    print(f"\n{'='*50}")
    print(f"REPORT DE INTEGRIDADE: {root_path.name}")
    print(f"{'='*50}")

    empty_dirs    = []
    stub_readmes  = []
    missing_inits = []

    for path in root_path.rglob("*"):
        if any(part.startswith(".") or part == "__pycache__" for part in path.parts):
            continue

        if path.is_dir():
            if not any(path.iterdir()):
                empty_dirs.append(path.relative_to(root_path))
            if "1_src" in path.parts and path.name != "1_src":
                if not (path / "__init__.py").exists():
                    missing_inits.append(path.relative_to(root_path))

        elif path.name == "README.md":
            try:
                content = path.read_text(encoding="utf-8").strip()
                lines   = [l for l in content.split("\n") if l.strip()]
                if len(lines) <= 2:
                    stub_readmes.append(path.relative_to(root_path))
            except (PermissionError, UnicodeDecodeError) as e:
                print(f"  [!] Não foi possível ler {path.relative_to(root_path)}: {e}")

    sections = [
        ("Pastas Vazias",           empty_dirs),
        ("READMEs por preencher",   stub_readmes),
        ("Pacotes sem __init__.py", missing_inits),
    ]
    for title, items in sections:
        print(f"\n[!] {title}: {len(items)}")
        for item in items:
            print(f"    └── {item}")

    if not any([empty_dirs, stub_readmes, missing_inits]):
        print("\n[V] Estrutura íntegra! Nada a reportar.")
    print(f"\n{'='*50}")


# --- Workflow Principal ---

def run(nome_proj: str = "", obj_proj: str = "") -> None:
    """!
    @brief Cria a estrutura do projeto ou audita se já estiver em 2_devtools/py.
    @param nome_proj Nome do projeto (opcional; usa input() como fallback).
    @param obj_proj  Pacote principal em 1_src (opcional; usa input() como fallback).
    """
    script_path = Path(__file__).resolve()

    if script_path.parts[-3:-1] == ("2_devtools", "py"):
        audit_project(script_path.parents[2])
        return

    if not nome_proj:
        nome_proj = input("Nome do Projeto: ").strip() or "novo_projeto"
    if not obj_proj:
        obj_proj = input("Objetivo do Projeto (pasta em src): ").strip() or "app"

    root     = Path(nome_proj).resolve()
    lib_path = script_path.parent / "lib.md"
    lib      = load_lib(lib_path)

    structure = [
        root / "0_docs/1_syllabus/md",
        root / "0_docs/1_syllabus/raw",
        root / "0_docs/2_api/doxygen",
        root / "0_docs/3_guides",
        root / f"1_src/{obj_proj}/models",
        root / f"1_src/{obj_proj}/pipeline",
        root / f"1_src/{obj_proj}/services",
        root / "2_devtools/py",
        root / "3_data/1_raw",
        root / "3_data/2_interim",
        root / "3_data/3_processed",
        root / "4_test",
    ]

    print(f"[*] Gerando andaime em: {root}")

    for folder in structure:
        folder.mkdir(parents=True, exist_ok=True)
        create_readme(folder / "README.md")

    for parent_folder in ["0_docs", "1_src", "2_devtools", "3_data", "4_test"]:
        create_readme(root / parent_folder / "README.md")

    # READMEs dinâmicos
    root_template = lib["readmes"].get("raiz", "# {nome_projeto}\n")
    create_file(root / "README.md", build_root_readme(root_template, nome_proj))

    devtools_template = lib["readmes"].get("2_devtools/README.md", "")
    commands_block    = lib["readmes"].get("2_devtools/comandos",   "")
    if devtools_template:
        create_file(
            root / "2_devtools/README.md",
            build_devtools_readme(devtools_template, lib["tool_meta"], commands_block),
        )

    # Arquivos de configuração (FILE)
    file_targets = {
        ".gitignore":    root / ".gitignore",
        "conftest.py":   root / "conftest.py",
        "Doxyfile":      root / "0_docs/2_api/doxygen/Doxyfile",
        "conventions.md": root / "0_docs/3_guides/conventions.md",
    }
    for lib_name, dest_path in file_targets.items():
        content = lib["files"].get(lib_name, "")
        if lib_name == "Doxyfile":
            content = content.replace("{project_name}", nome_proj)
        if content:
            create_file(dest_path, content)
        else:
            print(f"[!] Bloco FILE '{lib_name}' não encontrado em lib.md")

    create_file(root / f"1_src/{obj_proj}/pipeline/main.py", "# Entry point\n")

    # __init__.py — todas as subpastas de 1_src incluindo {obj_proj}
    for p in root.rglob("*"):
        if p.is_dir() and "1_src" in p.parts and p.name != "1_src":
            create_file(p / "__init__.py", "")
    create_file(root / "2_devtools/py/__init__.py", "")

    # Ferramentas (TOOL)
    if lib["tools"]:
        for filename, content in lib["tools"].items():
            create_file(root / "2_devtools/py" / filename, content)
    else:
        print("[!] Nenhuma ferramenta encontrada em lib.md")

    # Replicação do scaffold.py
    dest_scaffold = root / "2_devtools/py/scaffold.py"
    if dest_scaffold.exists():
        print("[i] scaffold.py já existe no destino, replicação ignorada.")
    else:
        create_file(dest_scaffold, script_path.read_text(encoding="utf-8"))

    # Replicação do lib.md
    dest_lib = root / "2_devtools/py/lib.md"
    if dest_lib.exists():
        print("[i] lib.md já existe no destino, replicação ignorada.")
    else:
        if lib_path.exists():
            create_file(dest_lib, lib_path.read_text(encoding="utf-8"))
        else:
            print("[!] lib.md não encontrado para replicação.")

    print(f"[V] Sucesso! Projeto '{nome_proj}' pronto.")
    print(f"[i] Para auditar: execute scaffold.py dentro de {root / '2_devtools' / 'py'}")


# --- CLI ---

def build_cli() -> argparse.ArgumentParser:
    """!
    @brief Constrói o parser de argumentos do CLI.
    @return ArgumentParser configurado.
    """
    parser = argparse.ArgumentParser(
        prog="scaffold",
        description="Gerenciador de estrutura de projetos Python.",
    )
    sub = parser.add_subparsers(dest="command")

    create_cmd = sub.add_parser("create", help="Cria um novo projeto.")
    create_cmd.add_argument("--name", default="", help="Nome do projeto.")
    create_cmd.add_argument("--obj",  default="", help="Pacote principal em 1_src.")

    audit_cmd = sub.add_parser("audit", help="Audita a estrutura de um projeto existente.")
    audit_cmd.add_argument(
        "--path", default="",
        help="Caminho raiz do projeto (padrão: dois níveis acima do script).",
    )

    docs_cmd = sub.add_parser("docs", help="Gera documentação Doxygen via gen_docs.py.")
    docs_cmd.add_argument(
        "--path", default="",
        help="Caminho raiz do projeto (padrão: dois níveis acima do script).",
    )

    return parser


def _run_gen_docs(script_path: Path) -> None:
    """!
    @brief Carrega e executa gen_docs.py via importlib.
    @param script_path Caminho do scaffold.py em execução.
    """
    gen_docs_path = script_path.parent / "gen_docs.py"
    if not gen_docs_path.exists():
        print("[!] gen_docs.py não encontrado em 2_devtools/py/")
        return
    spec = importlib.util.spec_from_file_location("gen_docs", gen_docs_path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.generate_docs()


if __name__ == "__main__":
    _parser = build_cli()
    _args   = _parser.parse_args()

    if _args.command == "create":
        run(nome_proj=_args.name, obj_proj=_args.obj)

    elif _args.command == "audit":
        _root = Path(_args.path).resolve() if _args.path else Path(__file__).resolve().parents[2]
        audit_project(_root)

    elif _args.command == "docs":
        _run_gen_docs(Path(__file__).resolve())

    else:
        run()