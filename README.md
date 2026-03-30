<!-- PATH: RAIZ DO PROJETO -->
# CourseBox

<!-- https://paletadecolores.online/pt/amarelo/mostarda/ -->
<!-- https://emojidb.org/alerta-emojis?utm_source=user_search -->

Repositório estratégico para a construção, tratamento e organização de cursos na plataforma [CourseBox](https://coursebox.ai).

## 📌 Índice

- [CourseBox](#coursebox)
  - [📌 Índice](#-índice)
  - [🎯 Objetivo](#-objetivo)
  - [🛠️ Instalação](#️-instalação)
    - [1. Instalando o VS Code](#1-instalando-o-vs-code)
    - [2. Clonando o repositório](#2-clonando-o-repositório)
    - [3. Instalando o `uv`](#3-instalando-o-uv)
    - [4. Doxygen (Opcional)](#4-doxygen-opcional)
    - [📌 Resumo](#-resumo)
  - [🚀 Setup](#-setup)
  - [🏗️ Estrutura do projeto](#️-estrutura-do-projeto)
    - [📁 0\_docs](#-0_docs)
    - [📁 1\_src](#-1_src)
    - [📁 2\_devtools](#-2_devtools)
    - [📁 3\_data](#-3_data)
  - [🛤️ Metodologia](#️-metodologia)
    - [Fase 1: Construção Individual](#fase-1-construção-individual)
    - [Fase 2: Reavaliação por Pares](#fase-2-reavaliação-por-pares)
    - [Fase 3: Refinamento Estético](#fase-3-refinamento-estético)
  - [💼 Fluxo de Trabalho](#-fluxo-de-trabalho)
  - [✳️ Quadro Resumo](#️-quadro-resumo)

## 🎯 Objetivo

Este repositório centraliza os procedimentos técnicos e pedagógicos para a criação de cursos estruturados via IA. A metodologia aqui proposta é aplicada em:

1.  **Curso ARCTEL "Empoderamento de Lideranças Femininas"**: Construção de material suplementar e substitutivo para as aulas síncronas (período de 19/05/2026 a 10/09/2026).
2.  **IAClube**: Desenvolvimento de cursos sobre Ferramentas de IA para o portal [iaclube.help](https://iaclube.help) e projetos vinculados a editais da FAPDF.

## 🛠️ Instalação

Antes de executar o projeto, siga as etapas abaixo para preparar o ambiente de desenvolvimento.

### 1. Instalando o VS Code

O **Visual Studio Code (VS Code)** é o editor de código recomendado para este projeto.

Ele oferece:

* suporte nativo a Python
* integração com Git
* extensões úteis para desenvolvimento

📥 Download: https://code.visualstudio.com/

Após instalar, recomenda-se adicionar as extensões:

* Python
* Pylance
* Markdown Preview

### 2. Clonando o repositório

O projeto está versionado com **Git**, que é um sistema de controle de versão.

Para obter uma cópia local do projeto (em uma pasta), utilize o comando no seu CMD ou PowerShell:

```bash id="j7x2rl"
git clone https://github.com/cadu-unb/CourseBox-Methodology.git
```

### 3. Instalando o `uv`

Este projeto utiliza o **uv** como gerenciador de pacotes para garantir velocidade e reprodutibilidade.

O `uv` é responsável por:

* instalar dependências
* gerenciar o ambiente Python
* executar o projeto

No Windows (PowerShell):

```powershell id="t2h8lw"
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 4. Doxygen (Opcional)

O **Doxygen** é uma ferramenta para geração automática de documentação do código.

Seu uso é opcional, sendo recomendado para:

* explorar a estrutura do código
* gerar documentação técnica em HTML

📥 Download: https://www.doxygen.nl/download.html

### 📌 Resumo

| Etapa | Ferramenta | Objetivo                          |
| ----- | ---------- | --------------------------------- |
| 1     | VS Code    | Editor de código                  |
| 2     | Git        | Clonar o repositório              |
| 3     | uv         | Gerenciar ambiente e dependências |
| 4     | Doxygen    | Gerar documentação (Opcional)     |


## 🚀 Setup

No terminal do VSCODE dentro do projeto:

```terminal
uv run
```

## 🏗️ Estrutura do projeto

A organização do repositório segue uma estrutura numérica para **facilitar navegação e leitura sequencial** das pastas, separando claramente:

* documentação
* código fonte
* ferramentas de desenvolvimento
* dados utilizados no processamento

```text
CourseBox-Methodology/
├── 0_docs
├── 1_src
├── 2_devtools
└── 3_data
```

Cada pasta possui uma responsabilidade específica dentro do projeto.

### 📁 0_docs

Contém **toda a documentação conceitual, metodológica e técnica** do projeto.

Esta pasta reúne materiais necessários para compreender a **metodologia pedagógica**, o **planejamento do curso** e a **documentação técnica do código**.

Estrutura principal:

```text
0_docs/
├── 0_methodology
├── 1_syllabus
├── 2_api
└── 3_guides
```

Subpastas:

* **0_methodology**
  Descreve a metodologia utilizada para transformar materiais educacionais em conteúdos estruturados.

* **1_syllabus**
  Contém os documentos de planejamento pedagógico do curso.

* **2_api**
  Documentação técnica do código gerada automaticamente com **Doxygen**.

* **3_guides**
  Guias técnicos do projeto, incluindo convenções de código e padrões de desenvolvimento.

### 📁 1_src

Contém **todo o código fonte do projeto**.

O código está organizado dentro do pacote principal `arctel`, seguindo uma arquitetura que separa **modelos de domínio, serviços e pipelines de processamento**.

Estrutura principal:

```text
1_src/
└── arctel/
    ├── models
    ├── services
    └── pipeline
```

Componentes principais:

* **models**
  Estruturas de dados utilizadas pelo sistema.

* **services**
  Implementação da lógica de negócio e processamento.

* **pipeline**
  Fluxos de processamento que orquestram serviços para executar tarefas completas, como conversão de vídeo em texto.

### 📁 2_devtools

Contém **ferramentas auxiliares utilizadas durante o desenvolvimento**.

Esses scripts não fazem parte do sistema principal, mas auxiliam na manutenção do projeto, automação de tarefas e inspeção da estrutura do repositório.

Exemplo:

```text
2_devtools/
└── py/
    └── file_tree.py
```

O script `file_tree.py` é utilizado para gerar automaticamente a **árvore de diretórios do projeto**.

### 📁 3_data

Armazena **dados utilizados nos pipelines do projeto**.

A estrutura segue o padrão comum em projetos de ciência de dados e engenharia de dados, separando **dados brutos** de **dados processados**.

```text
3_data/
├── 1_raw
└── 2_processed
```

Subpastas:

* **1_raw**
  Contém os dados originais utilizados como entrada nos processos.
  Esses dados devem permanecer **imutáveis**.

* **2_processed**
  Contém dados gerados a partir dos pipelines de processamento.

Essa separação facilita **reprodutibilidade, rastreabilidade e organização dos dados** ao longo do ciclo de desenvolvimento.

## 🛤️ Metodologia

O processo de trabalho é dividido em três fases fundamentais:

### Fase 1: Construção Individual
1.  **[Separação de Referências](0_docs/0_methodology/1_separation.md)**: Triagem de ementas e transcrição de aulas síncronas.
2.  **[Tratamento](0_docs/0_methodology/2_treatment.md)**: Elaboração de roteiros e alimentação da base de dados.
3.  **[Operação CourseBox](0_docs/0_methodology/3_operation.md)**: Configuração do assistente de IA na plataforma.
4.  **[Revisão Técnica](0_docs/0_methodology/4_review.md)**: Auditoria inicial dos resultados gerados pelo próprio operador. Deixar os capítulos desbloqueados.

### Fase 2: Reavaliação por Pares
5.  **[Feedback Cruzado](0_docs/0_methodology/5_feedback.md)**: Validação do conteúdo por outros membros da equipe.
6.  **[Melhoria Contínua](0_docs/0_methodology/6_improvement.md)**: Implementação de correções baseadas nos feedbacks.

### Fase 3: Refinamento Estético
7.  **[Personalização](0_docs/0_methodology/7_customization.md)**: Aperfeiçoamento da apresentação e experiência do usuário (UX).

## 💼 Fluxo de Trabalho

Foi fornecido um conjunto de documentos, listados na seção [Quadro Resumo](#quadro-resumo). No entanto, esses materiais abordam outros temas além daqueles especificamente previstos em cada aula. Além dos documentos, também teremos as gravações das aulas síncronas, que poderão ou não possuir arquivos de transcrição associados. Assim, será necessária uma etapa de transcrição (vide [_software_](0_docs/0_methodology/1_separation.md)) para tornar esse conteúdo textual disponível para as etapas subsequentes.

O segundo momento será crucial para definir a qualidade dos resultados obtidos com o assistente de IA da plataforma [CourseBox](https://www.coursebox.ai/). A partir das transcrições, iremos construir um conjunto de **[Notas de Aula](data/processed/README.md)** com o objetivo de [roteirizar o conteúdo](0_docs/0_methodology/2_treatment.md) abordado de forma precisa e estruturada. Esse processo de transformação poderá ser realizado com o auxílio de ferramentas de IA (ChatGPT, Gemini, Grok, entre outras). Em seguida, inicia-se uma etapa de revisão da estrutura proposta, acompanhada do desenvolvimento manual de conceitos, exemplos e demais elementos didáticos necessários.

De posse das Notas de Aula já aperfeiçoadas, com os assuntos descritos de maneira mais aprofundada, o arquivo será adicionado à pasta [Notas de Aula](data/processed/README.md) para fins de organização e controle. Em seguida, esse material será inserido na plataforma [CourseBox](https://www.coursebox.ai/). Nesse momento, serão realizados os procedimentos detalhados descritos na seção [Operação](3_operation.md).

Após o processamento do curso pela plataforma [CourseBox](https://www.coursebox.ai/), a primeira fase se encerra com uma revisão manual dos cursos gerados.

A segunda fase passa a depender de um protagonismo maior do grupo de trabalho. Cada integrante deverá realizar os cursos produzidos por colegas, registrando possíveis equívocos, inconsistências ou alucinações da IA que eventualmente tenham passado despercebidos durante a rodada inicial de revisões individuais.

Esse retorno será realizado em formato de feedback (ver modelo em [feedback](0_docs/0_methodology/5_feedback.md)).

Na etapa seguinte, cada autor de curso realizará a apuração individual das observações recebidas, analisando e incorporando as particularidades identificadas pelos colegas. Com isso, conclui-se a segunda fase do processo.

A última etapa da construção dos cursos consiste na definição manual de estrutura e design por parte dos membros responsáveis pelo design. O objetivo é realizar um refinamento estético dos cursos, aperfeiçoando sua apresentação visual e experiência de uso (vide [Personalizar](0_docs/0_methodology/7_personalize.md)).

<!-- Não altere o "Quadro Resumo" -->

## ✳️ Quadro Resumo

| Módulo | Título do Conteúdo | Datas | Duração | Ementa |
| :---: | :--- | :---: | :---: | :--- |
| **01** | [Impactos do Ecossistema Digital na Comunicação Social](https://drive.google.com/file/d/1FifuaZBgfqAmyBgaVdEdfKn4oPvHhw60/view?usp=drive_link) | 19/05 e 21/05 | 4h | Mudanças estruturais na organização, produção e consumo de comunicação social (rádio, TV e imprensa). Estudo de caso do Grupo Globo. |
| **02** | [Desenho regulatório responsivo](https://drive.google.com/file/d/1xJYEcPiN3cbVy2PaBFzTPyb62SDfv6T7/view?usp=sharing) | 26/05 e 28/05 | 4h | Conceitos fundamentais, fluxo regulatório, estágios da regulação responsiva, pirâmides responsivas e estudo de casos. |
| **03** | [Modelo regulatório pró-inovação](https://drive.google.com/file/d/1wx74GRWU7S9MSOeo6K-2G1VunWnnEX81/view?usp=sharing) | 02/06 a 09/06 | 6h | Ciência, tecnologia e inovação no ecossistema digital. Sandbox regulatório e experimentação no setor público brasileiro. |
| **04** | [Análise de Impacto Regulatório e Avaliação de Resultado](https://www.gov.br/anvisa/pt-br/assuntos/regulamentacao/air/saiba-mais-4) | 11/06 e 16/06 | 4h | Regulação com base em evidência, ciclo regulatório e etapas do processo de AIR e ARR. |
| **05** | [Tributação de Serviços Digitais](https://drive.google.com/file/d/1PVL4ngsbAgvy9DZCYNwg0v4fw_76WuMm/view?usp=sharing) | 18/06 a 25/06 | 6h | Oportunidades e modelos tributários para serviços digitais. Estudo de casos de exação ao redor do mundo. |
| **06** | Antitruste e Plataformas Digitais | 30/06 e 02/07 | 4h | Princípios do direito da concorrência, Digital Markets Act (DMA) e a experiência do CADE. (Referência a definir). |
| **07** | [Cadeia de Valor da Internet e a corrida pela Liderança Digital](https://drive.google.com/file/d/14qpYo0VT2c1kudV1spTjnp1pCza8pCNe/view?usp=sharing) | 07/07 a 16/07 | 8h | Arquitetura da cadeia de valor, estratégias de expansão de empresas de tecnologia e dinâmicas de mercado. |
| **08** | [Liberdade de Expressão no Ecossistema Digital](https://drive.google.com/file/d/1BqAD-iY1W0PrMCke_VkfACi1Ie9LwucG/view?usp=sharing) | 04/08 e 06/08 | 4h | Impacto das redes sociais na liberdade de expressão e o tratamento legislativo da questão no Brasil. |
| **09** | [Convergência tecnológica: impacto das OTT’s](https://drive.google.com/file/d/14qpYo0VT2c1kudV1spTjnp1pCza8pCNe/view?usp=sharing) | 11/08 a 20/08 | 8h | Arquiteturas tecnológicas, dinâmica de competição entre operadoras e OTT’s e impacto nas receitas (ARPU). |
| **10** | [Cenários prospectivos do futuro da Internet](https://drive.google.com/file/d/14qpYo0VT2c1kudV1spTjnp1pCza8pCNe/view?usp=sharing) | 25/08 a 03/09 | 8h | Personalização, privacidade, Web 3.0, Metaverso, IA, Blockchain e segurança cibernética. |
| **11** | Oficina com Lideranças Regulatórias | 08/09 e 10/09 | 4h | Papel da mulher na regulação e tecnologia, estratégias de liderança, inovação com equidade e redes de apoio. |
<!-- Não altere o "Quadro Resumo" -->

