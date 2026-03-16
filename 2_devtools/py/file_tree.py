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
