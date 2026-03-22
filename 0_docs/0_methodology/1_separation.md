<!-- PATH: 0_docs/0_methodology/1_separation.md -->

# 🧩 Etapa 1 — Coleta, Extração e Preparação de Dados

## 🎯 Objetivo da Etapa

Estabelecer a **ponte operacional entre o armazenamento em nuvem e o conteúdo textual bruto editável**, garantindo que todo material de entrada esteja:

* Disponível localmente
* Convertido para formato manipulável (`.txt`)
* Organizado conforme a governança do projeto

## 📌 Sumário

- [🧩 Etapa 1 — Coleta, Extração e Preparação de Dados](#-etapa-1--coleta-extração-e-preparação-de-dados)
  - [🎯 Objetivo da Etapa](#-objetivo-da-etapa)
  - [📌 Sumário](#-sumário)
  - [⚙️ Fluxo de Execução](#️-fluxo-de-execução)
  - [📥 Passo 1 — Coleta (Download dos Materiais)](#-passo-1--coleta-download-dos-materiais)
    - [🔍 Procedimento](#-procedimento)
    - [⚠️ Governança de Versionamento (Git)](#️-governança-de-versionamento-git)
    - [📁 Regra Crítica de Sincronização](#-regra-crítica-de-sincronização)
    - [🌿 Estratégia para Arquivos Pesados](#-estratégia-para-arquivos-pesados)
    - [⚠️ Regras adicionais](#️-regras-adicionais)
  - [🔄 Passo 2 — Extração (Conversão para Texto)](#-passo-2--extração-conversão-para-texto)
    - [🎯 Objetivo](#-objetivo)
    - [🛠️ Ferramental Obrigatório](#️-ferramental-obrigatório)
    - [📚 Documentação de Apoio](#-documentação-de-apoio)
    - [📌 Procedimento](#-procedimento-1)
  - [📦 Passo 3 — Armazenamento (Organização dos Dados)](#-passo-3--armazenamento-organização-dos-dados)
    - [📁 Destino Obrigatório](#-destino-obrigatório)
    - [🧭 Estrutura de Versionamento](#-estrutura-de-versionamento)
    - [✔ Regras](#-regras)
- [✅ Encerramento e Validação](#-encerramento-e-validação)
  - [✔ Checklist](#-checklist)
  - [🔍 Verificação final](#-verificação-final)
- [🔄 Encaminhamento](#-encaminhamento)
- [🧠 Resultado da Etapa](#-resultado-da-etapa)

## ⚙️ Fluxo de Execução

Execute esta etapa seguindo rigorosamente os 3 passos:

1. **Identificar** → localizar e baixar os arquivos de origem
2. **Extrair** → converter mídias para texto bruto (`.txt`)
3. **Armazenar** → organizar os arquivos no diretório correto

## 📥 Passo 1 — Coleta (Download dos Materiais)

### 🔍 Procedimento

1. Consulte o documento:

👉 **`0_docs/0_cloud.md`**

2. Identifique os materiais disponíveis:

   * PDFs
   * Vídeos de aula
   * Áudios

3. Realize o download dos arquivos necessários

### ⚠️ Governança de Versionamento (Git)

> **[CUIDADO]**
>
> O GitHub possui limite de **100MB por arquivo**.
> Arquivos de vídeo e áudio frequentemente ultrapassam esse limite.

### 📁 Regra Crítica de Sincronização

Você deve:

* ✅ Sincronizar apenas:

  **`3_data/2_processed/`**

* ❌ NÃO sincronizar:

  **`3_data/1_raw/`** *(exceto o `README.md`)*

### 🌿 Estratégia para Arquivos Pesados

Caso precise manipular arquivos grandes:

* Crie uma **branch temporária**
* Trabalhe localmente
* NÃO realize push de arquivos brutos pesados

### ⚠️ Regras adicionais

> **[CUIDADO]**
>
> O projeto já possui um `.gitignore` configurado para evitar versionamento de arquivos problemáticos.
> **Verifique antes de criar ou subir novos arquivos.**

## 🔄 Passo 2 — Extração (Conversão para Texto)

### 🎯 Objetivo

Converter todo conteúdo para o formato:

```text
.txt
```

### 🛠️ Ferramental Obrigatório

Utilize os scripts:

* **`text_extractor.py`** → para PDFs
* **`transcription.py`** → para áudio/vídeo

### 📚 Documentação de Apoio

Consulte:

* 👉 **`1_src/arctel/services/text_extractor.md`**
* 👉 **`1_src/arctel/services/transcription.md`**

### 📌 Procedimento

1. Execute os scripts apropriados
2. Gere arquivos `.txt` correspondentes
3. Valide se o conteúdo foi extraído corretamente

> **[CUIDADO]**
>
> Não prossiga com arquivos incompletos ou corrompidos.
> A qualidade da extração impacta todas as etapas seguintes.

## 📦 Passo 3 — Armazenamento (Organização dos Dados)

### 📁 Destino Obrigatório

Armazene os arquivos em:

**`3_data/2_processed/ArcTel/1_transcricao_inicial/`**

### 🧭 Estrutura de Versionamento

O pipeline segue 3 níveis de evolução:

```text
3_data/2_processed/ArcTel/
├── 1_transcricao_inicial/   ← Etapa 1 (este documento)
├── 2_notas_iniciais/        ← Etapa 2 (2_treatment.md)
└── 3_notas_finalizadas/     ← Etapa 2 (refino final)
```

### ✔ Regras

* Nomeie arquivos de forma consistente:

```text
aula_01.txt
aula_02.txt
```

* Garanta separação por aula ou módulo
* Evite arquivos agregados excessivamente grandes

# ✅ Encerramento e Validação

Antes de concluir a etapa:

## ✔ Checklist

* [ ] Todos os arquivos foram baixados corretamente
* [ ] Conversão para `.txt` realizada com sucesso
* [ ] Arquivos armazenados no diretório correto
* [ ] Nenhum arquivo pesado foi commitado indevidamente
* [ ] Estrutura respeita o padrão do projeto

## 🔍 Verificação final

* Confirme integridade na **branch principal (`main`)**
* Valide se não há conflitos ou arquivos indevidos

> **[CUIDADO]**
>
> Um erro de versionamento nesta etapa pode comprometer todo o repositório.

# 🔄 Encaminhamento

Após validação completa, prossiga para:

👉 **`2_treatment.md`** — Tratamento e Estruturação do Conteúdo

# 🧠 Resultado da Etapa

Ao final, você terá:

* Conteúdo bruto convertido em texto
* Estrutura organizada e versionada corretamente
* Base pronta para tratamento e refinamento

> 🚀 **Resumo Executivo**
>
> Esta etapa garante que os dados estejam **acessíveis, processáveis e governados corretamente**, evitando riscos operacionais e técnicos nas fases seguintes.
