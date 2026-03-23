# Análise para próximas etapas

Me ajude a indentificar a necessidade de dividir essa tarefas em um ou mais prompts para serem inseridos em sequência.

# Objetivos

1. [markdown] Desenvolver o processo relacionado ao arquivo `1_separation.md`.
2. [python3] Desenvolver algoritmo injeção em prompt.

# Contexto

Eu tenho um repositório onde defini uma metodologia para construir cursos na plataforma [CourseBox](https://coursebox.ai) com algum padrão de qualidade. No entanto, a sequência procedimental começa com uma bifurcação: "ArcTel" ou "PLIA-DF". 

Essa divisão foi necessária em razão das etapas `1_separation.md` (onde se coleta dos dados de arquivos de texto e vídeo) e `2_treatment.md` (a partir dos dados coletados se constroi um roteiro muito detalhado) que são particulares da **trilha "ArcTel"**.

Por outro lado, "PLIA-DF", representado por `1_preparation.md`, terá resultado final muito semelhante com o resultado da etapa `2_treatment.md`.

## 0_docs/0_methodology/README.md

```markdown="readme"
<!-- PATH: 0_docs/0_methodology/README.md -->
# Metodologia CourseBox

## 🎯 Objetivo
Descrever o fluxo metodológico de transformação de conteúdos educacionais.

## 🔄 Etapas da metodologia -> ArcTel (Concluida)

1. 👀 [Arquivos](0_cloud.md)
2. ✅ [Separação](1_separation.md)
3. ✅ [Tratamento](2_treatment.md)
4. ✅ [Operação](3_operation.md)
5. ✅ [Revisão](4_revisao.md)
6. ✅ [Feedback](5_feedback.md)
7. ✅ [Melhoria Contínua](6_improvement.md)
8. ✅ [Personalização](7_personalize.md)

## 🔄 Etapas da metodologia -> PLIA-DF (Em de)

1. ⚠️ [Elaboração](1_preparation.md)
2. ✅ [Operação](3_operation.md)
3. ✅ [Revisão](4_revisao.md)
4. ✅ [Feedback](5_feedback.md)
5. ✅ [Melhoria Contínua](6_improvement.md)
6. ✅ [Personalização](7_personalize.md)

## 🧠 Conceito
Cada etapa representa uma fase do pipeline pedagógico.

## FAC

Eu, @Cadu, fico a disposição para realizar correções no caso de eventuais ambiguidaes no corpo da metodologia e tirar dúvidas.
```

## Trilha "ArcTel"

Vamos considerar que esteja pronto.

## Trilha "PLIA-DF"

A grande diferênça entre o "PLIA-DF" e "ArcTel" é a origem da informação. Enquanto neste os dados vem de arquivos de texto e vídeo, o segundo depende exclusivamente de uma prompt bem estruturado e com contexto personalizado. 

### Personalização do Prompt

O papel deste prompt será construir um roteiro:
- **Curso Hands-on EAD** ensinado a fazer/utilizar a `{Habilidade}` com a(o) `{Ferramenta}`;
  - Título do curso => f"Já pensou utilizar o {Ferramenta} para fazer `{Habilidade_short}`?"
  - Subtítulo => f"Ao utilizar uma IA de `{name_AtributoFuncional}`, em especial, a ferramenta `{Ferramenta}` podemos fazer várias coisas, mas você qual o caminho das pedras para que `{Habilidade_long}` realmente brilhe. Venha ver conosco isso e muito mais."
  - SOLICITAR uma melhoria pela IA, dentro do contexto do roteiro gerado (vira uma submissão retroalimentada que depende do resultado do roteiro), tanto do Título quanto do Subtítulo para ficar apelativo, mas sem mentir sobre o conteúdo.
- **Duração:** MÍNIMA de **1h** e MÁXIMA de **4h**;
- **Público:** Professore (preferencialmente do Ensino Médio) da Secretária de Educação do Distrito Federal (SEDF);
- Estrutura do roteiro: 
  - Introdução;
    - Precisa abordar o `{description_AtributoFuncional}`.
  - 7 à 10 capítulos (cada um com uma atividade hands-on);
  - Quiz: cap 3-4, cap 6-7 e um quiz no último capítulo.
  - Resumo/conclusão.

### Dados para injeção

`3_data/0_json/pre-selecionado.json` :: Array<Group>
Group: { 
  id: string,
  FullNames: string,
  color: string(hex),
  items: Array<[id: string, name: string]> 
}

`3_data/0_json/packs_tasks_XXX.json` :: Array<FunctionalAttribute>
FunctionalAttribute: {
  FunctionalAttribute: string,
  FullNames: string,
  ShortNames: string,
  M10: Array<[title: string, description: string]>,
  M100: Array<string>,
  BigSet: Array<string>,
  Date: { initial_ingress: string(datetime), last_edited: string(date) },
  ShortDescription: string,
  FullDescription: string
}

> Observação: após o prefixo "packs_tasks_" e antes da extesão ".json" existirá um marcador para a versão atual dessa ED. Por exemplo, "a0.2" e "a0.3" na qual, a versão "a0.2" é mais antiga que "a0.3", e precisamos sempre verificar se existem duas ou mais versões e escolher a mais recente.

Dadas as ED acima, vou descrever a forma como vamos preencher `{Habilidade_short}`, `{Habilidade_long}`, `{name_AtributoFuncional}`, `{description_AtributoFuncional}` e `{Ferramenta}`. 

> Aceito sugestões de outras informações que podem ser anexadas ao prompt para enriquecer o contexto.


1. A chave `M10` possui uma lista de habilidade que foram observadas e classificadas em uma outra ED. Podemos utilizar `[M10][title]` para `{Habilidade_short}` e `[M10][description]` para `{Habilidade_long}`;
2. A chave `FullNames` identifica `{name_AtributoFuncional}`;
3. A chave `ShortDescription` é suficiente para caraterizar o atributo funcional definido. Vamos utiliza-la em `{description_AtributoFuncional}`. **Desafio:** Esse dado tem uma extesão aproximada de 60 á 80 palavras.
4. Em `pre-selecionado.json` temos `[items]` e dentro dele uma lista de dicionário com `"id"` e `"name"`. o primeiro serve apenas para ordenar os elementos enquanto o segundo será a `{Ferramenta}`.

# Retorno

## Organizar

Me ajude a organizar esse pensamentos.

## Análise crítica

- O que está faltando? me dê 3 sugestões.
- Algum problema estrutural muito grande na ideia?

