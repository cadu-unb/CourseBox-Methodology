<!-- PATH: 0_docs/0_methodology/1_separation.md -->
# 🧩 Etapa 1 — Triagem e Preparação Textual

## 📌 Índice 

- [🧩 Etapa 1 — Triagem e Preparação Textual](#-etapa-1--triagem-e-preparação-textual)
  - [📌 Índice](#-índice)
- [🎯 Introdução Estratégica](#-introdução-estratégica)
  - [Índice](#índice)
- [🔍 Diretrizes de Triagem](#-diretrizes-de-triagem)
  - [Índice](#índice-1)
  - [✅ Conteúdo Programático (Manter)](#-conteúdo-programático-manter)
  - [Índice](#índice-2)
  - [❌ Conteúdo Não Programático (Remover)](#-conteúdo-não-programático-remover)
  - [Índice](#índice-3)
  - [⚖️ Zona Cinzenta (Avaliar com Critério)](#️-zona-cinzenta-avaliar-com-critério)
  - [Índice](#índice-4)
- [🔗 Ponte Tecnológica](#-ponte-tecnológica)
  - [Índice](#índice-5)
  - [📄 Extração de PDFs](#-extração-de-pdfs)
  - [Índice](#índice-6)
  - [🎧 Processamento de Áudio/Vídeo](#-processamento-de-áudiovídeo)
  - [Índice](#índice-7)
  - [Índice](#índice-8)
- [📦 Output Esperado](#-output-esperado)
  - [✔ Limpo](#-limpo)
  - [Índice](#índice-9)
  - [✔ Estruturado](#-estruturado)
  - [Índice](#índice-10)
  - [✔ Segmentado](#-segmentado)
  - [Índice](#índice-11)
  - [✔ Pronto para IA](#-pronto-para-ia)
  - [Índice](#índice-12)
  - [Índice](#índice-13)
- [🧠 Resultado da Etapa](#-resultado-da-etapa)
  - [Índice](#índice-14)
  - [Índice](#índice-15)

# 🎯 Introdução Estratégica

A etapa de **Triagem e Preparação Textual** é o ponto mais crítico de todo o pipeline Arctel. É aqui que ocorre a separação entre:

* **Sinal** → conteúdo pedagógico relevante
* **Ruído** → redundâncias, desvios e elementos não instrucionais

Em ambientes de ensino assistidos por IA, como o Coursebox, a qualidade do input determina diretamente a qualidade do output. Este princípio é conhecido como:

> **Garbage In, Garbage Out (GIGO)**

Se conteúdos irrelevantes, ambíguos ou desorganizados forem fornecidos à IA:

* A estrutura do curso será inconsistente
* Os objetivos de aprendizagem serão diluídos
* A progressão pedagógica será comprometida

Por outro lado, um material bem triado permite:

* Geração automática de módulos coerentes
* Segmentação lógica de aulas
* Maior precisão na criação de atividades e avaliações

> ⚠️ **Aviso Crítico**
>
> Erros nesta etapa propagam-se por todo o pipeline e são **custosos de corrigir posteriormente**. Invista rigor aqui.

## Índice 

- [steriormente**. Invista rigor aqui.](#)

# 🔍 Diretrizes de Triagem

O operador deve atuar como um **curador técnico-pedagógico**, aplicando critérios claros para separar conteúdo útil de material descartável.

## Índice 

- [aros para separar conteúdo útil de material descartável.](#)

## ✅ Conteúdo Programático (Manter)

São elementos diretamente relacionados aos objetivos de aprendizagem:

* Conceitos fundamentais e definições
* Explicações estruturadas do conteúdo
* Exemplos didáticos relevantes
* Demonstrações práticas
* Exercícios comentados
* Sequências lógicas de raciocínio
* Conteúdo alinhado ao plano de ensino

## Índice 

- [Conteúdo alinhado ao plano de ensino](#)

## ❌ Conteúdo Não Programático (Remover)

Devem ser eliminados ou ignorados:

* Conversas informais (ex: saudações, comentários pessoais)
* Digressões fora do tema da aula
* Repetições desnecessárias
* Problemas técnicos (ex: “estão me ouvindo?”)
* Interações administrativas (ex: prazos, avisos institucionais)
* Pausas longas ou trechos sem conteúdo
* Ruído de transcrição (erros evidentes do OCR/ASR)

## Índice 

- [Ruído de transcrição (erros evidentes do OCR/ASR)](#)

## ⚖️ Zona Cinzenta (Avaliar com Critério)

Alguns conteúdos exigem julgamento:

* Perguntas de alunos → manter apenas se agregarem valor conceitual
* Analogias → manter se forem didaticamente relevantes
* Comentários contextuais → manter apenas se ajudam na compreensão

> 📌 **Nota**
>
> Em caso de dúvida, priorize **clareza pedagógica e objetividade**.

## Índice 

- [Em caso de dúvida, priorize **clareza pedagógica e objetividade**.](#)

# 🔗 Ponte Tecnológica

A execução desta etapa depende da correta utilização dos pipelines de extração e transcrição.

## Índice 

- [anscrição.](#)

## 📄 Extração de PDFs

Utilize o guia técnico:

👉 [text_extractor.md](../../1_src/arctel/services/text_extractor.md)

Responsável por:

* Extração estruturada de texto
* Preservação de layout
* OCR em documentos digitalizados

## Índice 

- [OCR em documentos digitalizados](#)

## 🎧 Processamento de Áudio/Vídeo

Utilize o guia técnico:

👉 [transcription.md](../../1_src/arctel/services/transcription.md)

Responsável por:

* Transcrição automática de aulas gravadas
* Conversão de fala em texto bruto

## Índice 

- [Conversão de fala em texto bruto](#)

> ⚠️ **Aviso Operacional**
>
> Sempre execute a triagem **após** a extração/transcrição completa.
> Nunca trabalhe diretamente com arquivos brutos (PDF/vídeo).

## Índice 

- [Nunca trabalhe diretamente com arquivos brutos (PDF/vídeo).](#)

# 📦 Output Esperado

Ao final desta etapa, o conteúdo deve estar:

## ✔ Limpo

* Sem ruídos ou conteúdos irrelevantes
* Sem duplicações
* Com linguagem clara

## Índice 

- [Com linguagem clara](#)

## ✔ Estruturado

Organizado por:

* Aula
* Tópico
* Subtópico

Exemplo:

```text
Aula 01 - Introdução a Circuitos

1. Conceito de circuito elétrico
2. Componentes básicos
3. Exemplos práticos
```

## Índice 

- [`](#)

## ✔ Segmentado

Idealmente em arquivos separados:

```text
aula_01.md
aula_02.md
aula_03.md
```

Ou:

```text
modulo_01/
├── aula_01.md
├── aula_02.md
```

## Índice 

- [`](#)

## ✔ Pronto para IA

O material deve estar:

* Semanticamente coerente
* Livre de ambiguidades
* Com progressão lógica clara

## Índice 

- [Com progressão lógica clara](#)

> 📌 **Nota Importante**
>
> A IA da Coursebox não “entende intenção pedagógica implícita”.
> Ela depende de **estrutura explícita e conteúdo bem delimitado**.

## Índice 

- [Ela depende de **estrutura explícita e conteúdo bem delimitado**.](#)

# 🧠 Resultado da Etapa

Ao concluir a Triagem e Preparação Textual, você terá:

* Um corpus limpo e confiável
* Conteúdo alinhado ao objetivo do curso
* Base sólida para automação nas próximas etapas

## Índice 

- [Base sólida para automação nas próximas etapas](#)

> 🚀 **Resumo Executivo**
>
> Esta etapa transforma conteúdo bruto em **matéria-prima pedagógica de alta qualidade**.
> Sem ela, não há automação confiável.

## Índice 

- [Sem ela, não há automação confiável.](#)

**Próxima etapa:** [`02_treatment.md`](2_treatment.md) — Tratamento e Refinamento do Conteúdo
