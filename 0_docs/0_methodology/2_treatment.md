<!-- PATH: 0_docs/0_methodology/2_treatment.md -->
# 🛠️ Etapa 2 — Tratamento de Conteúdo

## 📌 Índice
- [🛠️ Etapa 2 — Tratamento de Conteúdo](#️-etapa-2--tratamento-de-conteúdo)
  - [📌 Índice](#-índice)
- [🎯 Visão Geral](#-visão-geral)
- [🔐 Protocolo de Segurança (Backup)](#-protocolo-de-segurança-backup)
  - [📂 Estrutura esperada](#-estrutura-esperada)
  - [✔ Procedimento](#-procedimento)
- [🤖 Procedimento de Transformação via IA](#-procedimento-de-transformação-via-ia)
  - [🧰 Ferramentas recomendadas](#-ferramentas-recomendadas)
  - [📌 Passos](#-passos)
- [📋 Prompt de Referência (Bloco Copiável)](#-prompt-de-referência-bloco-copiável)
- [🔍 Fase de Revisão Humana](#-fase-de-revisão-humana)
  - [✔ Precisão Técnica](#-precisão-técnica)
  - [✔ Complementação de Exemplos](#-complementação-de-exemplos)
  - [✔ Controle de Tamanho](#-controle-de-tamanho)
  - [✔ Qualidade e profundidade](#-qualidade-e-profundidade)
- [📦 Critérios de Saída](#-critérios-de-saída)
  - [📁 Local de armazenamento](#-local-de-armazenamento)
  - [🏷️ Nomenclatura](#️-nomenclatura)
  - [🔄 Versionamento](#-versionamento)
- [🧠 Resultado da Etapa](#-resultado-da-etapa)

# 🎯 Visão Geral

A etapa de **Tratamento de Conteúdo** tem como objetivo transformar o material bruto (transcrições) em **Notas de Aula estruturadas, coerentes e pedagogicamente utilizáveis**.

Enquanto a etapa anterior focou em **remover ruído**, esta etapa foca em:

* Refinar a linguagem
* Organizar o conteúdo
* Estruturar o raciocínio didático
* Preparar o material para ingestão pela IA (Coursebox)

# 🔐 Protocolo de Segurança (Backup)

Antes de qualquer modificação, o operador **DEVE obrigatoriamente** preservar o material original.

## 📂 Estrutura esperada

```text id="x3k9wd"
data/
├── raw/
│   └── aula_01.txt
├── processed/
```

## ✔ Procedimento

1. Localize o arquivo de transcrição original
2. Copie para:

```bash id="3u7c9o"
data/raw/
```

3. Trabalhe exclusivamente em uma cópia dentro de:

```bash id="j2p8sl"
data/processed/
```

> ⚠️ **Nota Crítica**
>
> Nunca edite diretamente o arquivo original.
> O backup garante rastreabilidade, auditoria e possibilidade de retrabalho.

# 🤖 Procedimento de Transformação via IA

A transformação do conteúdo será realizada com apoio de ferramentas de IA generativa.

## 🧰 Ferramentas recomendadas

* ChatGPT
* Gemini
* Grok

## 📌 Passos

1. Acesse a ferramenta de IA
2. Anexe o arquivo `.txt` da transcrição
3. Utilize o **Prompt de Transformação** (abaixo)
4. Execute a geração
5. Copie o resultado gerado

> 📌 **Nota**
>
> Sempre forneça o arquivo completo. Evite colar trechos fragmentados, pois isso compromete a coerência global.

# 📋 Prompt de Referência (Bloco Copiável)

<!-- Para evitar bug de compreensão deixa uma espaço dedicado no documento para isso, ok? -->

```md id="prompt-transformacao"
# Role
Você é um Designer Instrucional Sênior especializado em transformar transcrições brutas de vídeo (Whisper) em Notas de Aula estruturadas, ricas e pedagogicamente organizadas.

# Contexto
Estou desenvolvendo um curso na plataforma Coursebox.ai. Recebi a transcrição bruta da aula "{nome_da_aula}" e preciso convertê-la em uma Apostila/Nota de Aula que servirá de base para o roteiro final do curso.

# Tarefa: Processamento de Transcrição para Notas de Aula
Com base no arquivo "{nome_do_arquivo}.txt" anexo, realize a estruturação do conteúdo seguindo estes pilares:

1. **Estrutura de Tópicos:** Organize o conteúdo em Seções e Subseções lógicas. Use títulos descritivos que facilitem a navegação do aluno.
2. **Parágrafo de contexto:** Cada Seções e Subseções, após seu título, deve possuir um parágrafo um parágrafo explicativa/descritivo com no mínimo 100 palavras e no máximo 150 palavras.
3. **Refinamento de Linguagem:** Transforme a linguagem falada (prolixa e com repetições) em uma linguagem escrita formal, porém acessível, mantendo todos os conceitos técnicos e detalhes explicados pelo professor.
4. **Elementos Didáticos:**
   - **Destaques:** Identifique e coloque em negrito termos-chave e conceitos fundamentais.
   - **Exemplos Práticos:** Extraia ou crie exemplos baseados na fala do professor para ilustrar pontos complexos.
   - **Boxes de Atenção:** Crie seções de "Dica do Especialista" ou "Atenção" para pontos onde o professor deu ênfase.
5. **Resumo Executivo:** Ao final, crie um "Quadro Resumo" com os pontos principais abordados na aula.

# Requisitos de Formatação
- Utilize Markdown para toda a estruturação.
- Use listas com marcadores (bullets) para procedimentos e características.
- Se houver fórmulas ou códigos mencionados, formate-os adequadamente em blocos específicos.

# Objetivo Final
O resultado deve ser uma Nota de Aula densa e detalhada, eliminando ruídos da fala, mas preservando 100% da riqueza técnica do conteúdo original.
```

# 🔍 Fase de Revisão Humana

Após o retorno da IA, o operador deve realizar uma validação criteriosa.

## ✔ Precisão Técnica

Verificar:

* Conceitos corretos
* Terminologia adequada
* Ausência de distorções geradas pela IA

## ✔ Complementação de Exemplos

Se necessário:

* Adicionar exemplos práticos
* Melhorar explicações ambíguas
* Inserir analogias úteis

## ✔ Controle de Tamanho

Garantir que:

* Parágrafos explicativos tenham entre **100–150 palavras**
* O conteúdo esteja equilibrado (nem superficial, nem excessivo)

> ⚠️ **Nota**
>
> A IA organiza bem o conteúdo, mas **não substitui validação técnica humana**.

## ✔ Qualidade e profundidade

Caso o resultado obtido apresente uma estrutura estritamente em tópicos, separe as seções e submeta-as novamente às ferramentas de IA. Solicite o aprofundamento de cada tema para enriquecer o conteúdo e dar mais densidade ao contexto.

# 📦 Critérios de Saída

Após validação, o material deve ser salvo seguindo padrão definido.

## 📁 Local de armazenamento

```text id="p6l2ys"
data/processed/
```

## 🏷️ Nomenclatura

```text id="8g3v1x"
aula_01_notas_v1.md
aula_02_notas_v1.md
```

## 🔄 Versionamento

Caso haja revisões:

```text id="l3z0pm"
aula_01_notas_v2.md
aula_01_notas_final.md
```

> 📌 **Nota**
>
> O versionamento permite rastrear melhorias e evitar perda de informação.

# 🧠 Resultado da Etapa

Ao final desta etapa, você terá:

* Notas de aula estruturadas
* Conteúdo validado tecnicamente
* Material pronto para ingestão na Coursebox

> 🚀 **Resumo Executivo**
>
> Esta etapa transforma transcrições em **conteúdo didático utilizável**, garantindo qualidade, clareza e consistência para as próximas fases do pipeline.

**Próxima etapa:** [`3_operation.md`](3_operation.md) — Operacionalização na Plataforma
