<!-- PATH: 1_src/arctel/services/text_extractor.md -->

# 📄 PDF Text Extractor

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![uv](https://img.shields.io/badge/Environment-uv-purple)
![OCR](https://img.shields.io/badge/OCR-Tesseract-green)
![Status](https://img.shields.io/badge/status-experimental-orange)

Pipeline de **extração híbrida de texto de PDFs**, capaz de processar tanto:

* **PDFs digitais (pesquisáveis)**
* **PDFs digitalizados (imagens)**

A solução utiliza:

* **PyMuPDF** para extração estruturada
* **Tesseract OCR** para fallback automático
* **Python 3** com ambiente gerenciado via **uv**

O pipeline preserva **ordem lógica de leitura**, evitando mistura de colunas ou blocos textuais.

---

## 📌 Índice

- [📄 PDF Text Extractor](#-pdf-text-extractor)
  - [📌 Índice](#-índice)
  - [🧠 Arquitetura](#-arquitetura)
  - [⚙️ Pré-requisitos de Sistema](#️-pré-requisitos-de-sistema)
    - [1️⃣ Tesseract OCR](#1️⃣-tesseract-ocr)
      - [Linux (Ubuntu/Debian)](#linux-ubuntudebian)
      - [macOS](#macos)
      - [Windows](#windows)
    - [2️⃣ (Opcional) Poppler](#2️⃣-opcional-poppler)
      - [Linux](#linux)
      - [macOS](#macos-1)
      - [Windows](#windows-1)
  - [📁 Estrutura do Projeto](#-estrutura-do-projeto)
    - [📍 Serviço de Extração](#-serviço-de-extração)
  - [💻 Guia de Uso (CLI)](#-guia-de-uso-cli)
    - [Extrair PDF completo](#extrair-pdf-completo)
    - [Extrair páginas específicas](#extrair-páginas-específicas)
    - [Resultado gerado](#resultado-gerado)
  - [🔍 Solução de Problemas](#-solução-de-problemas)
    - [Erro: `TesseractNotFoundError`](#erro-tesseractnotfounderror)
    - [✔️ Solução 1 — Adicionar ao PATH](#️-solução-1--adicionar-ao-path)
      - [Windows](#windows-2)
      - [Linux / macOS](#linux--macos)
    - [✔️ Solução 2 — Definir manualmente no código](#️-solução-2--definir-manualmente-no-código)
  - [📚 Dependências Python](#-dependências-python)
  - [🧩 Responsabilidade do Serviço](#-responsabilidade-do-serviço)
    - [📌 Objetivo](#-objetivo)
    - [🧠 Responsabilidades](#-responsabilidades)
    - [📏 Regras Arquiteturais](#-regras-arquiteturais)
  - [✨ Futuras melhorias](#-futuras-melhorias)

---

## 🧠 Arquitetura

O pipeline segue a estratégia **Hybrid Extraction**:

```
PDF
 │
 ├─ Extração estruturada (PyMuPDF)
 │        │
 │        ├─ Texto suficiente → salvar
 │        │
 │        └─ Texto insuficiente
 │
 └─ OCR automático (Tesseract)
          │
          └─ Consolidação em TXT
```

Critérios de fallback:

* Texto vazio
* Texto muito curto
* PDF composto apenas por imagens

---

## ⚙️ Pré-requisitos de Sistema

Algumas dependências **não são instaladas via pip**, pois são ferramentas de sistema.

### 1️⃣ Tesseract OCR

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-por
```

Opcional (suporte multilíngue):

```bash
sudo apt install tesseract-ocr-eng
```

---

#### macOS

Utilizando **Homebrew**:

```bash
brew install tesseract
```

Instalar idioma português:

```bash
brew install tesseract-lang
```

---

#### Windows

1️⃣ Baixar instalador oficial:

```
https://github.com/UB-Mannheim/tesseract/wiki
```

2️⃣ Instalar normalmente.

3️⃣ Adicionar ao **PATH do sistema**:

```
C:\Program Files\Tesseract-OCR
```

---

> 📌 **Nota**
>
> O idioma `por` melhora significativamente OCR de documentos em português.

---

### 2️⃣ (Opcional) Poppler

Caso o pipeline utilize `pdf2image`, será necessário instalar **Poppler**.

#### Linux

```bash
sudo apt install poppler-utils
```

#### macOS

```bash
brew install poppler
```

#### Windows

Baixar:

```
https://github.com/oschwartz10612/poppler-windows
```

Depois adicionar `bin/` ao PATH.

---

## 📁 Estrutura do Projeto

```
project-root
│
├─ 0_docs/
│
├─ 1_src/
│   │
│   ├─ services/
│   │   │
│   │   ├─ text_extractor.py
│   │   └─ README.md
│   │
│   ├─ pipelines/
│   └─ utils/
│
├─ pyproject.toml
└─ README.md
```

---

### 📍 Serviço de Extração

```
1_src/arctel/services/text_extractor.py
```

Responsável por:

* Extração estruturada
* Detecção de páginas escaneadas
* Execução de OCR
* Consolidação de texto

---

## 💻 Guia de Uso (CLI)

O script pode ser executado diretamente via **linha de comando**.

---

### Extrair PDF completo

```bash
uv run 1_src/arctel/services/text_extractor.py documento.pdf saida.txt
```

---

### Extrair páginas específicas

Formato:

```
1,5,10-12
```

Exemplo:

```bash
uv run 1_src/arctel/services/text_extractor.py documento.pdf saida.txt --pages "1,5,10-12"
```

---

### Resultado gerado

```
saida.txt
```

Formato:

```
===== Página 1 =====
conteúdo extraído...

===== Página 2 =====
conteúdo extraído...
```

---

## 🔍 Solução de Problemas

### Erro: `TesseractNotFoundError`

Esse erro ocorre quando o Python não encontra o executável do Tesseract.

Exemplo:

```
pytesseract.pytesseract.TesseractNotFoundError
```

---

### ✔️ Solução 1 — Adicionar ao PATH

Certifique-se de que o executável está no PATH.

#### Windows

Adicionar:

```
C:\Program Files\Tesseract-OCR
```

Depois reiniciar o terminal.

---

#### Linux / macOS

Verificar instalação:

```bash
which tesseract
```

Se não aparecer caminho:

```
/usr/bin/tesseract
```

Reinstalar.

---

### ✔️ Solução 2 — Definir manualmente no código

```python
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

> 📌 **Nota**
>
> Em servidores Linux normalmente **não é necessário configurar manualmente**, pois o binário já está no PATH.

---

## 📚 Dependências Python

Principais bibliotecas utilizadas:

| Biblioteca  | Função                      | Instalado |
| ----------- | --------------------------- | --------- |
| PyMuPDF     | Extração estruturada de PDF |    ✅    |
| pytesseract | Interface Python para OCR   |    ✅    |
| Pillow      | Manipulação de imagens      |    ✅    |

---

## 🧩 Responsabilidade do Serviço

### 📌 Objetivo

Implementar **extração robusta de texto documental**.

---

### 🧠 Responsabilidades

* Processamento de PDFs
* Fallback automático para OCR
* Preservação de layout textual
* Consolidação de texto

---

### 📏 Regras Arquiteturais

* Não depender diretamente de **pipelines de orquestração**
* Manter lógica **isolada e reutilizável**
* Garantir **resiliência a documentos heterogêneos**

---

## ✨ Futuras melhorias

* OCR paralelo (multiprocessing)
* Extração automática de tabelas
* Exportação estruturada (JSON)
* Detecção de layout com IA

---

**Autor:** Carlos Eduardo Papa
**Projeto:** CourseBox
