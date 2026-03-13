import os
import sys

def normalize_extensions(extension_list: list[str]) -> list[str]:
    """!
    @brief Normaliza uma lista de extensões para o formato '.ext'.
    @param extension_list Lista de strings com as extensões.
    @return Lista de extensões em letras minúsculas e iniciadas com ponto.
    """
    if not extension_list:
        return []
    
    normalized = []
    for ext in extension_list:
        ext = ext.lower().strip()
        if ext and not ext.startswith('.'):
            ext = f".{ext}"
        normalized.append(ext)
    return normalized

def should_include_item(item_name: str, relative_path: str, is_dir: bool, config: dict) -> bool:
    """!
    @brief Verifica se um arquivo ou pasta deve ser incluído na árvore.
    @param item_name Nome do arquivo ou pasta.
    @param relative_path Caminho relativo do item.
    @param is_dir Booleano indicando se o item é um diretório.
    @param config Dicionário contendo as listas de filtros (ignored_dirs, visible_extensions, etc).
    @return True se o item deve ser incluído, False caso contrário.
    """
    # Converter para minúsculo para comparação case-insensitive
    item_name_lower = item_name.lower()
    
    if is_dir:
        # Ignora pastas ocultas ou que estão na blacklist
        if item_name.startswith('.') or item_name in config['ignored_dirs'] or relative_path in config['ignored_dirs']:
            return False
        return True
    
    # Lógica para arquivos
    extension = os.path.splitext(item_name_lower)[1]
    
    # 1. Verifica se está na blacklist de extensões
    if extension in config['ignored_extensions']:
        return False
    
    # 2. Verifica se o nome do arquivo está explicitamente na whitelist
    if item_name in config['visible_files'] or relative_path in config['visible_files']:
        return True
    
    # 3. Verifica a whitelist de extensões (Se vazia, aceita tudo que não foi bloqueado antes)
    if not config['visible_extensions']:
        return True
    
    return extension in config['visible_extensions']

def generate_file_tree(base_path: str, current_path: str, prefix: str = "", config: dict = None) -> tuple[list[str], list[str], dict]:
    """!
    @brief Gera recursivamente a representação visual da árvore e a lista de caminhos.
    @param base_path Caminho raiz do projeto.
    @param current_path Caminho que está sendo explorado no momento.
    @param prefix Prefixo de indentação para a árvore visual.
    @param config Dicionário de configurações de filtros.
    @return Uma tupla contendo (linhas_da_arvore, lista_de_caminhos, estatisticas).
    """
    lines = []
    file_paths = []
    stats = {"files": 0, "dirs": 0}
    
    try:
        items = os.listdir(current_path)
    except PermissionError:
        return [f"{prefix} [Acesso Negado]"], [], stats
    except FileNotFoundError:
        return [f"{prefix} [Diretório não encontrado]"], [], stats

    # Filtragem inicial
    filtered_items = []
    for item in items:
        full_path = os.path.join(current_path, item)
        rel_path = os.path.relpath(full_path, base_path).replace("\\", "/")
        is_directory = os.path.isdir(full_path)
        
        if should_include_item(item, rel_path, is_directory, config):
            filtered_items.append((item, full_path, rel_path, is_directory))

    filtered_items.sort(key=lambda x: (not x[3], x[0].lower())) # Pastas primeiro, depois arquivos

    for i, (name, full_path, rel_path, is_directory) in enumerate(filtered_items):
        is_last = (i == len(filtered_items) - 1)
        connector = "└── " if is_last else "├── "
        
        lines.append(f"{prefix}{connector}{name}")
        
        if is_directory:
            stats["dirs"] += 1
            new_prefix = prefix + ("    " if is_last else "│   ")
            sub_lines, sub_paths, sub_stats = generate_file_tree(base_path, full_path, new_prefix, config)
            lines.extend(sub_lines)
            file_paths.extend(sub_paths)
            stats["files"] += sub_stats["files"]
            stats["dirs"] += sub_stats["dirs"]
        else:
            stats["files"] += 1
            file_paths.append(rel_path)
            
    return lines, file_paths, stats

def save_output(filename: str, content: list[str]) -> bool:
    """!
    @brief Salva o conteúdo em um arquivo de texto.
    @param filename Nome do arquivo de destino.
    @param content Lista de strings a serem salvas.
    @return True se salvo com sucesso, False caso contrário.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(content))
        return True
    except Exception as e:
        print(f"❌ Erro ao salvar {filename}: {e}")
        return False

def main():
    # --- Configurações ---
    target_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    
    config = {
        "ignored_dirs" : [
            '__pycache__', '.git', 'node_modules', '.vscode', #'.venv' 
        ],
        "visible_extensions" : normalize_extensions( # Aceita com ou sem ponto
            [
                # 'html', 'css', 'js', 'json' 
            ]
        ), 
        "ignored_extensions" : normalize_extensions( # Blacklist
            [
                'log', 'tmp', 'exe', 'txt'
            ]
        ), 
        "visible_files" : [ # Nomes específicos
            # 'README.md', 'package.json'
        ] 
    }

    print(f"\n🔍 Analisando diretório: {os.path.abspath(target_directory)}")
    
    # Geração
    tree_body, path_list, summary = generate_file_tree(target_directory, target_directory, config=config)
    
    # Adiciona a raiz na visualização
    final_tree = ["CourseBox-Methodology/"] + tree_body

    # Salvamento
    success_tree = save_output("tree_focada.txt", final_tree)
    success_paths = save_output("caminhos.txt", path_list)

    # --- Relatório de Retorno ---
    print("\n" + "="*40)
    print("📊 RELATÓRIO DE EXECUÇÃO")
    print("="*40)
    
    if success_tree and success_paths:
        print(f"✅ Sucesso! Arquivos gerados:")
        print(f"   - tree_focada.txt  ({len(final_tree)} linhas)")
        print(f"   - caminhos.txt     ({len(path_list)} arquivos listados)")
        print("-" * 40)
        print(f"📁 Pastas processadas: {summary['dirs']}")
        print(f"📄 Arquivos incluídos: {summary['files']}")
    else:
        print("⚠️  Houve problemas ao salvar alguns arquivos de saída.")
    
    print("="*40 + "\n")

if __name__ == "__main__":
    main()