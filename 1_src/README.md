# Estrutura da pasta `arctel`

Este diretório contém o **código principal do sistema ARCTEL**.

A organização segue princípios de separação de responsabilidades para facilitar **manutenção, escalabilidade e clareza arquitetural** do projeto.

---

## 📌 Índice

- [Estrutura da pasta `arctel`](#estrutura-da-pasta-arctel)
  - [📌 Índice](#-índice)
  - [Visão Geral da Estrutura](#visão-geral-da-estrutura)
  - [`core`](#core)
    - [`models`](#models)
    - [`types`](#types)
  - [`services`](#services)
  - [`pipeline`](#pipeline)
  - [Regras gerais de organização](#regras-gerais-de-organização)
      - [core](#core-1)
      - [services](#services-1)
      - [pipeline](#pipeline-1)

---

## Visão Geral da Estrutura

```text
arctel/
├── core
│   ├── models
│   └── types
├── services
└── pipeline
```

Cada pasta possui um papel específico dentro da arquitetura do sistema.

A ideia central é separar:

* **estrutura de dados**
* **regras de negócio**
* **fluxos operacionais**

---

## `core`

O diretório **core** contém os **elementos fundamentais do domínio do sistema**.

Aqui ficam as definições mais básicas do projeto, que podem ser utilizadas por qualquer outro módulo.

O conteúdo de `core` deve ser:

* estável
* reutilizável
* independente de infraestrutura
* independente de pipelines

Estrutura:

```text
core/
├── models
└── types
```

---

### `models`

A pasta **models** contém as **estruturas de dados principais do domínio do sistema**.

Esses modelos representam entidades manipuladas pelo projeto.

Exemplos possíveis no ARCTEL:

* transcrições de vídeo
* metadados de aula
* estruturas de conteúdo educacional
* representação de documentos

Exemplo de estrutura:

```text
models/
├── transcript.py
├── video_metadata.py
└── lecture.py
```

Exemplo simples de modelo:

```python
class Transcript:
    def __init__(self, text: str, language: str):
        self.text = text
        self.language = language
```

Boas práticas para `models`:

* representar **dados do domínio**
* evitar lógica pesada
* manter classes simples
* priorizar clareza estrutural

---

### `types`

A pasta **types** contém **tipos auxiliares e estruturas leves usadas em todo o sistema**.

Ela é usada para centralizar:

* tipos compartilhados
* enums
* estruturas auxiliares
* contratos de dados simples

Exemplos de arquivos:

```text
types/
├── language.py
├── status.py
└── enums.py
```

Exemplo:

```python
from enum import Enum

class Language(Enum):
    PT = "portuguese"
    EN = "english"
```

Boas práticas para `types`:

* manter tipos reutilizáveis
* evitar lógica de negócio
* usar para padronizar valores no sistema

---

## `services`

Contém a **lógica de negócio do sistema**.

Aqui ficam os algoritmos e processos que manipulam os modelos do domínio.

Exemplos de responsabilidades:

* processamento de transcrição
* limpeza de texto
* geração de material didático
* integração com APIs de IA
* processamento de linguagem natural

Estrutura típica:

```text
services/
├── transcription_service.py
├── text_cleaning_service.py
└── summarization_service.py
```

Exemplo:

```python
def clean_transcript(text: str) -> str:
    return text.strip()
```

Boas práticas:

* concentrar **regras de negócio**
* usar `models` como entrada e saída
* evitar dependência direta de pipelines
* manter funções reutilizáveis

---

## `pipeline`

Contém **fluxos operacionais completos do sistema**.

Um pipeline coordena múltiplos serviços para executar uma tarefa maior.

Exemplo típico no ARCTEL:

```text
vídeo → transcrição → limpeza → estruturação → material didático
```

Estrutura possível:

```text
pipeline/
├── video_to_text.py
└── generate_material.py
```

Exemplo simplificado:

```python
from arctel.services.transcription_service import transcribe

def video_to_text(video_path):
    transcript = transcribe(video_path)
    return transcript
```

Boas práticas:

* pipelines devem **orquestrar processos**
* lógica complexa deve ficar em `services`
* evitar duplicação de código

---

## Regras gerais de organização

#### core

Contém **fundamentos do domínio**.

* estruturas principais
* tipos compartilhados
* conceitos centrais do sistema

#### services

Contém **regras de negócio e algoritmos**.

* processamento
* integrações
* lógica principal do sistema

#### pipeline

Contém **fluxos completos de execução**.

* coordenação de serviços
* execução de tarefas complexas

---

##O que NÃO colocar neste pacote

Não colocar dentro de `arctel`:

* scripts de manutenção
* ferramentas utilitárias
* experimentos
* scripts administrativos

Esses elementos devem ficar fora do pacote principal, por exemplo:

```text
scripts/
devtools/
```

---

##Objetivo desta organização

Essa estrutura busca:

* facilitar leitura do código
* reduzir acoplamento entre módulos
* permitir crescimento do sistema
* manter separação clara de responsabilidades
* tornar o projeto mais sustentável a longo prazo
