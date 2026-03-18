<!-- PATH: 1_src/services/transcription.md -->

# 🎧 Video Transcription Service

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![uv](https://img.shields.io/badge/Environment-uv-purple)
![Whisper](https://img.shields.io/badge/AI-Whisper-green)
![Status](https://img.shields.io/badge/status-experimental-orange)

Pipeline de **transcrição automática de vídeos**, utilizando modelos da **OpenAI Whisper**, com foco em:

* Extração de áudio de vídeos
* Transcrição em português (ou multilíngue)
* Geração de arquivos `.txt` em UTF-8

---

## 📌 Índice

- [🎧 Video Transcription Service](#-video-transcription-service)
  - [📌 Índice](#-índice)
  - [🧠 Arquitetura](#-arquitetura)
  - [⚙️ Pré-requisitos de Sistema](#️-pré-requisitos-de-sistema)
    - [1️⃣ FFmpeg (OBRIGATÓRIO)](#1️⃣-ffmpeg-obrigatório)
      - [Linux (Ubuntu/Debian)](#linux-ubuntudebian)
      - [macOS (Homebrew)](#macos-homebrew)
      - [Windows](#windows)
    - [2️⃣ (Opcional) Aceleração com GPU](#2️⃣-opcional-aceleração-com-gpu)
  - [� Estrutura do Projeto](#-estrutura-do-projeto)
    - [📍 Serviço de Transcrição](#-serviço-de-transcrição)
  - [💻 Guia de Uso (CLI)](#-guia-de-uso-cli)
    - [Transcrever vídeo](#transcrever-vídeo)
    - [Definir modelo Whisper](#definir-modelo-whisper)
    - [Definir diretório de saída](#definir-diretório-de-saída)
    - [Saída gerada](#saída-gerada)
  - [🔍 Solução de Problemas](#-solução-de-problemas)
    - [Erro: FFmpeg não encontrado](#erro-ffmpeg-não-encontrado)
    - [✔️ Solução](#️-solução)
    - [Erro: Whisper lento ou travando](#erro-whisper-lento-ou-travando)
      - [Possíveis causas:](#possíveis-causas)
    - [✔️ Solução](#️-solução-1)
    - [Erro: Falta de memória](#erro-falta-de-memória)
      - [✔️ Solução](#️-solução-2)
  - [📚 Dependências Python](#-dependências-python)
  - [🧩 Responsabilidade do Serviço](#-responsabilidade-do-serviço)
    - [📌 Objetivo](#-objetivo)
    - [🧠 Responsabilidades](#-responsabilidades)
    - [📏 Regras Arquiteturais](#-regras-arquiteturais)
  - [✨ Futuras melhorias](#-futuras-melhorias)

---

## 🧠 Arquitetura

O pipeline segue o fluxo:

```text
Vídeo (.mp4)
 │
 ├─ Extração de áudio (MoviePy)
 │
 └─ Transcrição (Whisper)
          │
          └─ Arquivo TXT (UTF-8)
```

---

## ⚙️ Pré-requisitos de Sistema

Diferente do pipeline de PDF, aqui não há dependências como Tesseract ou Poppler, mas existem requisitos importantes:

### 1️⃣ FFmpeg (OBRIGATÓRIO)

O Whisper e o MoviePy dependem do **FFmpeg** para processamento de áudio/vídeo.

---

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install ffmpeg
```

---

#### macOS (Homebrew)

```bash
brew install ffmpeg
```

---

#### Windows

1️⃣ Baixar:

```
https://ffmpeg.org/download.html
```

2️⃣ Extrair o conteúdo

3️⃣ Adicionar ao PATH:

```
C:\ffmpeg\bin
```

---

> ⚠️ **Aviso**
>
> Sem o FFmpeg corretamente configurado, o pipeline **não funcionará**.

---

### 2️⃣ (Opcional) Aceleração com GPU

Se estiver usando GPU NVIDIA:

```bash
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

---

> 📌 **Nota**
>
> A GPU acelera significativamente a transcrição com modelos maiores (`medium`, `large`).

---

## 📁 Estrutura do Projeto

```text
project-root
│
├─ 0_docs/
│
├─ 1_src/
│   │
│   ├─ services/
│   │   │
│   │   ├─ text_extractor.py
│   │   ├─ transcription.py
│   │   └─ transcription.md
│   │
│   ├─ pipelines/
│   └─ utils/
│
├─ pyproject.toml
├─ requirements.txt
└─ README.md
```

---

### 📍 Serviço de Transcrição

```text
1_src/services/transcription.py
```

Responsável por:

* Extração de áudio
* Transcrição com IA (Whisper)
* Persistência em TXT

---

## 💻 Guia de Uso (CLI)

O script pode ser executado diretamente via terminal.

---

### Transcrever vídeo

```bash
python 1_src/services/transcription.py video.mp4
```

---

### Definir modelo Whisper

Modelos disponíveis:

| Modelo | Velocidade   | Qualidade |
| ------ | ------------ | --------- |
| tiny   | Muito rápida | Baixa     |
| base   | Rápida       | Média     |
| small  | Média        | Boa       |
| medium | Lenta        | Muito boa |
| large  | Muito lenta  | Excelente |

Exemplo:

```bash
python 1_src/services/transcription.py video.mp4 --model medium
```

---

### Definir diretório de saída

```bash
python 1_src/services/transcription.py video.mp4 --output ./saida
```

---

### Saída gerada

```
video_transcricao.txt
```

---

## 🔍 Solução de Problemas

### Erro: FFmpeg não encontrado

Mensagem comum:

```
MoviePy error: failed to read the duration of file
```

---

### ✔️ Solução

Verificar instalação:

```bash
ffmpeg -version
```

Se não funcionar:

* Reinstalar FFmpeg
* Garantir que está no PATH

---

### Erro: Whisper lento ou travando

#### Possíveis causas:

* CPU fraca
* Modelo muito grande

---

### ✔️ Solução

Usar modelo menor:

```bash
--model base
```

---

### Erro: Falta de memória

#### ✔️ Solução

* Reduzir modelo (`tiny` ou `base`)
* Processar vídeos menores

---

> 📌 **Nota**
>
> Whisper carrega o modelo inteiro em memória — isso impacta diretamente RAM.

---

## 📚 Dependências Python

| Biblioteca | Função                          |
| ---------- | ------------------------------- |
| whisper    | Transcrição de áudio            |
| moviepy    | Extração de áudio de vídeo      |
| pathlib    | Manipulação moderna de caminhos |

---

## 🧩 Responsabilidade do Serviço

### 📌 Objetivo

Transformar vídeos em texto de forma automatizada.

---

### 🧠 Responsabilidades

* Extração de áudio
* Transcrição com IA
* Persistência de dados

---

### 📏 Regras Arquiteturais

* Não depender de pipelines diretamente
* Manter isolamento da lógica
* Garantir reuso e extensibilidade

---

## ✨ Futuras melhorias

* Exportação em SRT (legendas)
* Transcrição com timestamps
* Diarização (identificação de falantes)
* Processamento em lote (batch)
* Paralelismo

---

**Autor:** Carlos Eduardo Papa
**Projeto:** CourseBox
