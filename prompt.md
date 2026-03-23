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

--- resposta

1. Organização dos Pensamentos (Pipeline)

A separação em três momentos garante que a lógica do script não se misture com a qualidade pedagógica do texto.

    Prompt A (O Arquiteto de Dados - Python): Focado estritamente no algoritmo de busca, comparação de versões (a0.2 vs a0.3) e extração dos campos JSON.

    Prompt B (O Engenheiro de Prompt - Template): Focado na construção do "Master Prompt" que receberá as variáveis. Aqui definimos o tom de voz para os professores da SEDF.

    Prompt C (O Revisor Pedagógico - Refino): Focado na "submissão retroalimentada" que você mencionou, para tornar títulos e subtítulos mais apelativos após o roteiro estar pronto.

2. Análise Crítica: O que está faltando?

Aqui estão 3 sugestões para enriquecer o contexto e evitar que o roteiro fique genérico:

    Contextualização Regional (Distrito Federal): Como o público são professores da SEDF, o prompt deve injetar diretrizes ou termos comuns ao Currículo em Movimento do DF. Sugerir que as atividades hands-on utilizem exemplos voltados à realidade local (ex: problemas urbanos de Brasília, bioma Cerrado) aumenta muito a adesão dos professores.

    Mapeamento de Competências (BNCC): Já que o público é de professores de Ensino Médio, seria valioso pedir à IA que associe cada capítulo do roteiro a uma competência ou habilidade da BNCC. Isso poupa um trabalho imenso para o professor que for utilizar o curso.

    Critério de Complexidade das Tarefas: No JSON, você tem M10, M100 e BigSet. Seria interessante definir que capítulos iniciais usem M10 (mais simples) e os capítulos finais (7-10) busquem elementos do BigSet (mais complexos), criando uma curva de aprendizado real.

3. Problemas Estruturais

Identifiquei um ponto de atenção no Volume de Contexto vs. Janela de Token:

    O "Gargalo" do JSON: Se você tentar injetar todo o packs_tasks_XXX.json em um único prompt junto com o pre-selecionado.json, a IA pode se perder ou "cortar" detalhes da FullDescription.

    Solução: O seu algoritmo Python deve fazer o pré-processamento. Ele não deve enviar o JSON inteiro, mas apenas os campos exatos que você mapeou (FullNames, ShortDescription, e o item específico do M10). Isso mantém o prompt limpo e focado.

Próximo Passo sugerido

Gostaria que eu elaborasse o primeiro prompt da sequência (Prompt A), focado no algoritmo Python que gerencia as versões dos arquivos a0.x e prepara o dicionário de injeção?

Ou prefere que eu comece desenhando o Template do Roteiro (Prompt B) com o foco pedagógico para a SEDF?