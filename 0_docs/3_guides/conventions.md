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
