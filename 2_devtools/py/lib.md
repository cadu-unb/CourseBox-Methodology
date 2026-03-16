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
