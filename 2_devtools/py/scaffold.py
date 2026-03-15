import os
from pathlib import Path

# --- Conteúdos dos arquivos específicos ---

CONTENT_DOXYFILE = """# Nome do projeto
PROJECT_NAME = "CourseBox-Methodology"

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
"""

CONTENT_CONVENTIONS = '''# Coding Conventions

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

```
snake_case
```

#### ✔ Bom

```
services
data_processing
video_pipeline
```

#### ❌ Ruim

```
VideoProcessing
video-processing
VideoPipeline
```

## Nomenclatura de arquivos e módulos

Arquivos Python também devem utilizar **snake_case**.

Formato:

```
snake_case.py
```

#### ✔ Bom

```
video_to_text.py
transcription_service.py
file_tree.py
```

#### ❌ Ruim

```
VideoToText.py
video-to-text.py
FileTree.py
```

Evitar:

* nomes genéricos (`utils.py`, `helpers.py`)
* nomes muito longos
* abreviações não padronizadas

## Classes

Classes devem utilizar **PascalCase**.

Formato:

```
PascalCase
```

#### ✔ Bom

```python
class Transcript:
    pass

class VideoMetadata:
    pass
```

#### ❌ Ruim

```python
class transcript:
    pass

class video_metadata:
    pass
```

## Funções

Funções devem usar **snake_case**.

Formato:

```
snake_case()
```

#### ✔ Bom

```python
def transcribe_video(video_path):
    pass


def clean_transcript(text):
    pass
```

#### ❌ Ruim

```python
def TranscribeVideo():
    pass


def cleanTranscript():
    pass
```

## Variáveis

Variáveis também usam **snake_case**.

#### ✔ Bom

```python
video_path = "lecture.mp4"
transcript_text = ""
video_duration = 3600
```

#### ❌ Ruim

```python
videoPath = "lecture.mp4"
VideoPath = "lecture.mp4"
v = "lecture.mp4"
```

Evitar variáveis de **uma letra**, exceto em loops simples:

```python
for i in range(10):
    pass
```

## Constantes

Constantes devem usar **UPPER_CASE**.

#### ✔ Bom

```python
MAX_VIDEO_DURATION = 7200
DEFAULT_LANGUAGE = "pt"
```

#### ❌ Ruim

```python
maxVideoDuration = 7200
defaultLanguage = "pt"
```

## Modelos de tipos (Python 3)

O projeto deve utilizar **type hints modernos** do Python 3.

Sempre que possível, funções devem declarar tipos de entrada e saída.

#### Exemplo básico

```python
def clean_text(text: str) -> str:
    return text.strip()
```

### Tipos comuns

#### Listas

```python
def process_videos(videos: list[str]) -> list[str]:
    pass
```

#### Dicionários

```python
def load_metadata() -> dict[str, str]:
    pass
```

#### Opcional

```python
from typing import Optional

def load_transcript(path: str) -> Optional[str]:
    pass
```

#### União de tipos

Python 3.10+

```python
def parse_input(data: str | bytes) -> str:
    pass
```

#### Estruturas de dados com `dataclass`

Recomendado para modelos simples.

```python
from dataclasses import dataclass

@dataclass
class Transcript:
    text: str
    language: str
```

## Docstrings (padrão Doxygen)

Todas as funções públicas devem possuir **docstrings no padrão Doxygen**.

Formato básico:

```
"""
Descrição da função.

@param parametro descrição
@return descrição do retorno
"""
```

### Exemplo correto

```python
def transcribe_video(video_path: str) -> str:
    """
    Transcreve o áudio de um vídeo.

    @param video_path Caminho do arquivo de vídeo
    @return Texto transcrito
    """
```

### Exemplo incorreto

```python
def transcribe_video(video_path):
    # faz a transcrição
```

## Imports

Imports devem seguir esta ordem:

1. biblioteca padrão do Python
2. bibliotecas externas
3. módulos do projeto

Exemplo:

```python
import os
import pathlib

import numpy as np

from arctel.services.transcription_service import transcribe
```

Evitar:

```python
from module import *
```

## Padrões para pipelines de dados

Pipelines devem seguir alguns princípios estruturais.

#### Pipeline deve:

* orquestrar serviços
* conectar etapas de processamento
* evitar lógica pesada

#### Estrutura recomendada

```
pipeline/
├── video_to_text.py
├── generate_material.py
```

#### Exemplo de pipeline

```python
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
```

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
'''

# Dicionário de ferramentas para a pasta 2_devtools/py
CONTENT_DEVTOOLS = {
    "file_tree.py": '''import os
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
''',
    
}

def create_file(file_path, content=""):
    """
    @brief Writes content to a file, creating directories if needed.
    @param file_path (Path) Destination path.
    @param content (str) Text to write.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def create_readme(file_path, project_root):
    """
    @brief Creates a README with a PATH header.
    @param file_path (Path) Path to the README.md.
    @param project_root (Path) Root of the project for relative calculation.
    """
    try:
        rel_path = file_path.relative_to(project_root)
    except ValueError:
        rel_path = file_path.name
    
    header = f"\\n\\n# {file_path.parent.name}\\n"
    create_file(file_path, header)

def check_integrity(root_path):
    """
    @brief Audits the project structure for empty folders and stub READMEs.
    @param root_path (Path) The project root to scan.
    @return (dict) A report containing gaps found.
    """
    report = {"empty_dirs": [], "stub_readmes": [], "missing_inits": []}
    
    for path in root_path.rglob("*"):
        # Ignora pastas de sistema/ambiente
        if any(part.startswith('.') or part == "__pycache__" for part in path.parts):
            continue
            
        if path.is_dir():
            # Verifica pastas vazias
            if not any(path.iterdir()):
                report["empty_dirs"].append(str(path.relative_to(root_path)))
            
            # Verifica falta de __init__.py em pastas de código (1_src)
            if "1_src" in path.parts and not (path / "__init__.py").exists():
                if path.name not in ["1_src"]:
                    report["missing_inits"].append(str(path.relative_to(root_path)))

        elif path.name == "README.md":
            # Verifica se o README só tem o header de PATH
            with open(path, "r", encoding="utf-8") as f:
                lines = [l for l in f.readlines() if l.strip()]
                if len(lines) <= 2 and "PATH:" in lines[0]:
                    report["stub_readmes"].append(str(path.relative_to(root_path)))
                    
    return report

def run_scaffold():
    """
    @brief Main workflow for creating or auditing the project structure.
    """
    current_dir = Path.cwd()
    
    # Válvula de Segurança: Verifica se estamos dentro da pasta de devtools
    if current_dir.parts[-2:] == ("2_devtools", "py"):
        project_root = current_dir.parents[2]
        print(f"--- MODO AUDITORIA ATIVADO ({project_root.name}) ---")
        report = check_integrity(project_root)
        
        print(f"\\n[!] Pastas vazias found: {len(report['empty_dirs'])}")
        for d in report["empty_dirs"]: print(f"  - {d}")
            
        print(f"\\n[!] READMEs ainda 'não documentados': {len(report['stub_readmes'])}")
        for r in report["stub_readmes"]: print(f"  - {r}")

        print(f"\\n[!] Pacotes Python sem __init__.py: {len(report['missing_inits'])}")
        for i in report["missing_inits"]: print(f"  - {i}")
        return

    # Modo Criação
    p_name = input("Nome do Projeto: ").strip() or "meu_projeto"
    p_obj = input("Objetivo (pasta src): ").strip() or "core"
    root = Path(p_name)

    # Definição expandida
    structure = [
        root / "0_docs/1_syllabus/md",
        root / "0_docs/2_api/doxygen",
        root / "0_docs/3_guides",
        root / "0_docs/4_archived",
        root / "0_docs/5_assets",
        root / f"1_src/{p_obj}/models",
        root / f"1_src/{p_obj}/pipeline",
        root / f"1_src/{p_obj}/services",
        root / "2_devtools/py",
        root / "3_data/0_external",
        root / "3_data/1_raw",
        root / "3_data/2_processed",
        root / "4_tests"
    ]

    for folder in structure:
        folder.mkdir(parents=True, exist_ok=True)
        create_readme(folder / "README.md", root)

    # Arquivos raiz
    create_readme(root / "README.md", root)
    create_file(root / ".gitignore", "__pycache__/\\n.env\\n.vscode/")
    create_file(root / ".env.example", "API_KEY=your_key_here")

    # Inits e Main
    for p in root.rglob("*/"):
        if "1_src" in p.parts and p.name not in ["1_src", p_obj]:
            create_file(p / "__init__.py", "")

    # Inserindo ferramentas do DevTools
    for filename, content in CONTENT_DEVTOOLS.items():
        create_file(root / "2_devtools/py" / filename, content)

    # Auto-replicação do scaffold
    with open(__file__, "r", encoding="utf-8") as f:
        create_file(root / "2_devtools/py/scaffold.py", f.read())

    print(f"\\n[V] Estrutura '{p_name}' criada. Ferramenta movida para 2_devtools/py/scaffold.py")

if __name__ == "__main__":
    run_scaffold()