# Persona

Você é um especialista em gerenciamento e desenvolvimento de projeto.

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
2. A chave `FullNames` identifica `{name_AtributoFuncional}`. Note que existe uma razão fundamental para que a chave exista na duas EDs, que é necessidade de uma informação completar a outra;
3. A chave `ShortDescription` é suficiente para caraterizar o atributo funcional definido. Vamos utiliza-la em `{description_AtributoFuncional}`. **Desafio:** Esse dado tem uma extesão aproximada de 60 á 80 palavras.
4. Em `pre-selecionado.json` temos `[items]` e dentro dele uma lista de dicionário com `"id"` e `"name"`. o primeiro serve apenas para ordenar os elementos enquanto o segundo será a `{Ferramenta}`.

### Equipe

A composição dessas informações é um aspecto fundamental. Isto é, uma vez que tomamos o primeiro termo de `Group` (de `3_data/0_json/pre-selecionado.json`), teremos uma lista de ferramentas (dentro de `[items]`) e precisaremos comparar o `FullNames` de `Group` com o `FullNames` de `FunctionalAttribute` (de `3_data/0_json/packs_tasks_XXX.json`) para assim correlacionar os dados com a devida precisão;

Para a construção acontecerá por meio de uma equipe. Por essa precisamos de mais uma ED:

`3_data/0_json/equipe.json` :: Array<Operador>
Operador: { 
  matricula: string,
  nome: string,
  color: string(hex),
  ferramentas: Array<Group> 
}
Group: { 
  id: string,
  FullNames: string,
  color: string(hex),
  items: Array<[id: string, name: string, cache:bool]> 
}

> Não precisamos pensar em como as atividades serão dividias ou memos quantos operadores existiram. Deixaremos isso para outra etapa.

#### Cache

Considerando que o operador já recebeu a lista de ferramentas que irá trabalhar, precisamos de um nível de controle. Por essa razão, adicionei `cache:bool`. O que pode nos ajudar a realizar o controle tanto a nível local quanto para controle da execução de tarefas em uma futura dashboard de desenpenho da equipe.

# Retorno

## Organizar

Me ajude a organizar esse pensamentos.

## Análise crítica

- O que está faltando? me dê 3 sugestões.
- Algum problema estrutural muito grande na ideia?

# Anexos

trecho de `packs_tasks_XXX.json`:

```json
[
    {
        "FunctionalAttribute": "agentic",
        "FullNames": "Agêntica (Agentic AI)",
        "ShortNames": "Agêntica",
        "M10": [
            [
                "Definição de Objetivos",
                "Avalia interpretação, formalização, priorização e adaptação de objetivos, incluindo restrições, dependências, métricas de sucesso e rastreabilidade ao longo da missão."
            ],
            [
                "Planejamento Estratégico",
                "Mede criação e ajuste de planos, análise de riscos, alocação de recursos, definição de cronogramas e integração contínua de feedback em ambientes dinâmicos."
            ],
            [
                "Percepção e Coleta de Informações",
                "Analisa monitoramento de dados, avaliação de fontes, integração de informações heterogêneas, detecção de padrões, inferência sob incerteza e alerta de eventos críticos."
            ],
            [
                "Tomada de Decisão Autônoma",
                "Avalia escolha entre alternativas, uso de heurísticas, gestão de incerteza, consideração ética, explicabilidade e adaptação contínua baseada em novas evidências."
            ],
            [
                "Execução e Coordenação de Ações",
                "Mede execução confiável de ações, coordenação paralela, interação com sistemas externos, validação de resultados e manutenção de consistência de estados."
            ],
            [
                "Aprendizado e Melhoria Contínua",
                "Analisa autoavaliação, aprendizado com experiências, ajuste de parâmetros, reutilização de soluções, transferência de conhecimento e manutenção de histórico evolutivo."
            ],
            [
                "Colaboração e Negociação",
                "Avalia comunicação entre agentes, negociação de recursos e prazos, coordenação com humanos, resolução de conflitos e manutenção de transparência operacional."
            ],
            [
                "Autonomia e Autorregulação",
                "Mede operação sem supervisão, autodiagnóstico, gestão de recursos, segurança, conformidade ética e adaptação a múltiplas missões simultâneas."
            ],
            [
                "Raciocínio e Resolução de Problemas",
                "Analisa estruturação de problemas complexos, raciocínio lógico e probabilístico, simulações, validação de soluções e adaptação criativa sob restrições severas."
            ],
            [
                "Interação e Experiência do Usuário",
                "Avalia interpretação de linguagem natural, esclarecimento de requisitos, explicação de decisões, personalização da comunicação e garantia de controle humano e segurança."
            ]
        ],
        "M100": [
            "1. Interpretar objetivos gerais fornecidos pelo usuário ou outro sistema",
            "2. Converter objetivos vagos em metas claras e mensuráveis",
            "3. Identificar restrições (tempo, recursos, orçamento, políticas)",
            "4. Avaliar prioridades de múltiplos objetivos concorrentes",
            "5. Formular sub-objetivos alinhados ao objetivo principal",
            "6. Identificar dependências entre tarefas",
            "7. Mapear resultados esperados e métricas de sucesso",
            "8. Detectar inconsistências ou conflitos entre objetivos",
            "9. Adaptar objetivos conforme novas informações surgem",
            "10. Documentar objetivos de forma rastreável",
            "11. Criar planos de ação de curto, médio e longo prazo",
            "12. Selecionar estratégias adequadas a cada contexto",
            "13. Calcular custo-benefício de alternativas de ação",
            "14. Estimar riscos e impactos potenciais",
            "15. Definir cronogramas realistas",
            "16. Criar pontos de verificação para avaliar progresso",
            "17. Ajustar planos em tempo real diante de mudanças",
            "18. Integrar feedback contínuo ao planejamento",
            "19. Distribuir recursos de forma eficiente",
            "20. Manter resiliência contra falhas parciais",
            "21. Monitorar múltiplas fontes de dados (sensores, APIs, documentos)",
            "22. Identificar informações relevantes ao contexto da missão",
            "23. Avaliar a confiabilidade das fontes",
            "24. Coletar dados de forma contínua ou sob demanda",
            "25. Detectar padrões e anomalias em tempo real",
            "26. Integrar dados heterogêneos em uma visão unificada",
            "27. Filtrar ruído e redundância informacional",
            "28. Atualizar modelos internos com novos dados",
            "29. Realizar inferências a partir de dados incompletos",
            "30. Alertar para informações críticas ou urgentes",
            "31. Avaliar múltiplas opções de ação",
            "32. Utilizar heurísticas e algoritmos de otimização",
            "33. Balancear velocidade de decisão com precisão",
            "34. Considerar consequências éticas e legais",
            "35. Lidar com incerteza e informações parciais",
            "36. Executar decisões sem supervisão direta",
            "37. Revisar decisões diante de novas evidências",
            "38. Justificar escolhas de forma transparente",
            "39. Evitar viés indesejado na escolha",
            "40. Integrar preferências do usuário no processo decisório",
            "41. Executar ações físicas ou digitais conforme plano",
            "42. Interagir com sistemas externos via API, CLI ou UI",
            "43. Coordenar múltiplas tarefas em paralelo",
            "44. Controlar sequências de ações complexas",
            "45. Lidar com interrupções e retomadas",
            "46. Sincronizar operações com outros agentes humanos ou artificiais",
            "47. Gerir filas e prioridades de execução",
            "48. Validar resultados de cada ação antes de prosseguir",
            "49. Automatizar tarefas repetitivas de forma segura",
            "50. Garantir consistência de dados e estados após execução",
            "51. Avaliar desempenho próprio",
            "52. Comparar resultados obtidos com resultados esperados",
            "53. Identificar erros e causas-raiz",
            "54. Aprender com casos de sucesso e fracasso",
            "55. Incorporar novas técnicas ou algoritmos",
            "56. Ajustar parâmetros de operação com base em experiência",
            "57. Aprender preferências individuais do usuário",
            "58. Reutilizar soluções previamente bem-sucedidas",
            "59. Transferir conhecimento para outros agentes",
            "60. Manter histórico para evolução futura",
            "61. Comunicar-se claramente com outros agentes",
            "62. Negociar prazos, recursos e prioridades",
            "63. Compartilhar dados e resultados relevantes",
            "64. Coordenar esforços com equipes humanas",
            "65. Assumir papéis diferentes em grupos (líder, executor, suporte)",
            "66. Resolver conflitos entre agentes ou usuários",
            "67. Criar compromissos e acordos operacionais",
            "68. Manter transparência nas interações",
            "69. Respeitar protocolos de comunicação",
            "70. Incentivar cooperação entre agentes heterogêneos",
            "71. Operar sem supervisão constante",
            "72. Monitorar seu próprio consumo de recursos",
            "73. Detectar e prevenir ações prejudiciais",
            "74. Pausar ou abortar ações perigosas",
            "75. Ajustar ritmo de execução conforme contexto",
            "76. Autodiagnosticar falhas e corrigi-las",
            "77. Cumprir normas éticas e legais de forma autônoma",
            "78. Lidar com múltiplas missões simultâneas",
            "79. Reconfigurar-se para novas tarefas",
            "80. Preservar segurança de dados e sistemas sob seu controle",
            "81. Identificar problemas complexos e estruturá-los",
            "82. Usar raciocínio lógico e probabilístico",
            "83. Criar hipóteses e testá-las",
            "84. Selecionar métodos de solução adequados",
            "85. Integrar conhecimento de múltiplas áreas",
            "86. Usar simulações para prever resultados",
            "87. Resolver problemas sob pressão de tempo",
            "88. Encontrar soluções criativas para restrições severas",
            "89. Validar soluções antes da aplicação real",
            "90. Adaptar soluções existentes a novos contextos",
            "91. Interpretar instruções em linguagem natural",
            "92. Fazer perguntas para esclarecer requisitos",
            "93. Apresentar resultados de forma clara e acessível",
            "94. Fornecer visualizações de progresso",
            "95. Personalizar interações conforme perfil do usuário",
            "96. Explicar raciocínios e decisões",
            "97. Permitir intervenções humanas em qualquer momento",
            "98. Fornecer opções alternativas de ação",
            "99. Adaptar tom e formalidade da comunicação",
            "100. Garantir que a experiência do usuário seja satisfatória e segura"
        ],
        "BigSet": [
            "Objetivos",
            "Planejamento",
            "Percepção",
            "Decisão",
            "Execução",
            "Aprendizado",
            "Colaboração",
            "Autonomia",
            "Raciocínio",
            "Interação"
        ],
        "Date": {
            "initial_ingress": "2025-11-12 10:22:05",
            "last_edited": "2026-02-06"
        },
        "ShortDescription": "Uma IA agêntica, ou Agentic AI, refere-se a um tipo de inteligência artificial que vai além de simplesmente executar tarefas pré-programadas. Em vez disso, ela é capaz de definir seus próprios objetivos, planejar as etapas para alcançá-los e executar ações de forma autônoma em um ambiente dinâmico. Pense nela como uma IA que pode \"pensar por si mesma\" em um nível mais estratégico.",
        "FullDescription": "Uma IA agêntica, ou Agentic AI, refere-se a um tipo de inteligência artificial que vai além de simplesmente executar tarefas pré-programadas. Em vez disso, ela é capaz de definir seus próprios objetivos, planejar as etapas para alcançá-los e executar ações de forma autônoma em um ambiente dinâmico. Pense nela como uma IA que pode \"pensar por si mesma\" em um nível mais estratégico.\nPrincipais características de uma IA Agêntica:\n•\tAutonomia: Ela não precisa de instruções detalhadas a cada passo. Uma vez que um objetivo é definido (ou ela o define), ela age por conta própria para alcançá-lo.\n•\tDefinição de objetivos: Uma IA agêntica pode, em certos cenários, até mesmo inferir ou definir seus próprios objetivos com base em informações e no contexto em que opera.\n•\tPlanejamento: Ela é capaz de criar um plano de ação, quebrando um objetivo maior em subtarefas e organizando a sequência de execuções.\n•\tExecução e adaptação: A IA executa as ações planejadas e, crucialmente, monitora o ambiente e o progresso em tempo real. Se algo mudar ou um obstáculo surgir, ela pode adaptar seu plano e tomar novas decisões para continuar avançando em direção ao objetivo.\n•\tPercepção e raciocínio: Para agir autonomamente, ela precisa perceber o ambiente, processar informações e raciocinar sobre como suas ações afetarão o estado do mundo.\nComo funciona?\nImagine uma IA agêntica como um ciclo contínuo de:\n1.\tObservar: Capturar informações do ambiente.\n2.\tOrientar: Analisar e interpretar essas informações, definindo (ou redefinindo) o objetivo.\n3.\tPlanejar: Criar uma estratégia para atingir o objetivo.\n4.\tAgir: Executar as ações planejadas.\nEste ciclo se repete, permitindo que a IA ajuste seu comportamento e suas estratégias à medida que o ambiente muda ou novos dados se tornam disponíveis."
    },
    {
        "FunctionalAttribute": "data",
        "FullNames": "Análise ou Visualização de Dados",
        "ShortNames": "Dados",
        "M10": [
            [
                "Coleta e Integração de Dados",
                "Avalia conexão, extração e unificação de dados de múltiplas fontes, incluindo bancos, APIs, web, sensores, redes sociais e fluxos em tempo real."
            ],
            [
                "Preparação e Qualidade de Dados",
                "Mede limpeza, padronização, correção de erros, tratamento de ausências, outliers, criação de variáveis derivadas e segmentação para análise confiável."
            ],
            [
                "Análise Estatística",
                "Analisa aplicação de estatística descritiva e inferencial, correlações, regressões, testes de hipóteses e análises multivariadas."
            ],
            [
                "Visualização de Dados",
                "Avalia criação de gráficos estáticos e interativos para explorar, comparar e comunicar padrões, tendências e distribuições de dados."
            ],
            [
                "Análise Geoespacial",
                "Mede visualização e análise de dados espaciais, incluindo mapas temáticos, camadas, densidade, rotas, coordenadas GPS e integrações cartográficas."
            ],
            [
                "Modelagem Preditiva e Aprendizado de Máquina",
                "Analisa criação, otimização e explicação de modelos preditivos, classificação, segmentação, detecção de anomalias e análise de sentimentos."
            ],
            [
                "Dashboards e Relatórios",
                "Avalia construção de painéis interativos, relatórios executivos e técnicos, atualizações automáticas, filtros dinâmicos e distribuição de resultados."
            ],
            [
                "Automação e Integração",
                "Mede automação de análises, pipelines de dados, agendamentos, versionamento e integração com ferramentas externas, APIs, ETL e plataformas corporativas."
            ],
            [
                "Colaboração e Acessibilidade",
                "Analisa recursos colaborativos, controle de acesso, histórico de versões, acessibilidade, suporte multilíngue e compatibilidade com múltiplos dispositivos."
            ],
            [
                "Análise Avançada e Inovação",
                "Avalia storytelling automatizado, análise em linguagem natural, simulações, visualização imersiva, assistentes inteligentes e explicabilidade de modelos."
            ]
        ],
        "M100": [
            "1. Conectar-se a bancos de dados SQL e NoSQL",
            "2. Importar dados de planilhas (Excel, CSV, ODS, TSV)",
            "3. Coletar dados via APIs REST e GraphQL",
            "4. Extrair dados de páginas web (web scraping)",
            "5. Integrar dados de sensores IoT",
            "6. Conectar a ferramentas de BI como Power BI e Tableau",
            "7. Unificar dados de múltiplas fontes heterogêneas",
            "8. Automatizar processos de coleta periódica",
            "9. Importar dados de redes sociais",
            "10. Lidar com dados de streaming em tempo real",
            "11. Detecção de valores ausentes",
            "12. Preenchimento de valores ausentes (imputação)",
            "13. Remoção de duplicatas",
            "14. Normalização de dados",
            "15. Padronização de formatos (datas, moedas, medidas)",
            "16. Detecção de outliers",
            "17. Conversão de tipos de dados",
            "18. Correção automática de erros de digitação",
            "19. Criação de variáveis derivadas",
            "20. Filtragem e segmentação de dados",
            "21. Cálculo de médias, medianas e modas",
            "22. Medidas de dispersão (variância, desvio-padrão)",
            "23. Correlação entre variáveis",
            "24. Testes de hipóteses (t-test, chi-square)",
            "25. Análise de regressão linear e múltipla",
            "26. Análise de regressão logística",
            "27. Séries temporais",
            "28. Análise de clusters",
            "29. Análise de componentes principais (PCA)",
            "30. Análise de variância (ANOVA)",
            "31. Criar gráficos de barras e colunas",
            "32. Criar gráficos de linhas",
            "33. Criar gráficos de pizza e rosca",
            "34. Criar histogramas",
            "35. Criar gráficos de dispersão",
            "36. Criar heatmaps (mapas de calor)",
            "37. Criar boxplots",
            "38. Criar gráficos de área",
            "39. Criar gráficos de radar",
            "40. Criar gráficos de Gantt",
            "41. Mapas coropléticos",
            "42. Mapas de pontos",
            "43. Mapas com rotas e trajetos",
            "44. Mapas de calor geográficos",
            "45. Integração com Google Maps e Mapbox",
            "46. Visualização de coordenadas GPS",
            "47. Representação de dados geoespaciais 3D",
            "48. Sobreposição de camadas (layers)",
            "49. Filtragem por área geográfica",
            "50. Análise geoespacial de densidade",
            "51. Prever tendências de séries temporais",
            "52. Criar modelos de classificação",
            "53. Criar modelos de regressão",
            "54. Detectar padrões ocultos",
            "55. Segmentar clientes automaticamente",
            "56. Prever churn de clientes",
            "57. Recomendação de produtos/serviços",
            "58. Otimização de modelos com AutoML",
            "59. Detecção de anomalias",
            "60. Análise de sentimento em textos",
            "61. Criar dashboards interativos",
            "62. Atualização automática de dados em tempo real",
            "63. Exportar relatórios em PDF, Excel e imagens",
            "64. Criação de relatórios narrativos automáticos",
            "65. Painéis com filtros dinâmicos",
            "66. Comparação de períodos (ano a ano, mês a mês)",
            "67. Alertas automáticos por e-mail",
            "68. Compartilhamento de dashboards online",
            "69. Criação de relatórios executivos",
            "70. Geração de relatórios técnicos detalhados",
            "71. Agendar tarefas de análise",
            "72. Integrar com Google Sheets",
            "73. Conectar com Slack, Teams e e-mails para envio de alertas",
            "74. Enviar resultados para APIs externas",
            "75. Conectar com ferramentas de ETL",
            "76. Integração com plataformas de e-commerce",
            "77. Exportar resultados para CRM",
            "78. Automação de atualizações de dashboards",
            "79. Criação de pipelines de dados",
            "80. Versionamento de dados e análises",
            "81. Controle de acesso por usuário",
            "82. Comentários e anotações em gráficos",
            "83. Exportar visualizações em formatos compatíveis com apresentações",
            "84. Otimização para mobile",
            "85. Acessibilidade para deficientes visuais",
            "86. Suporte a múltiplos idiomas",
            "87. Histórico de versões de relatórios",
            "88. Recursos para trabalho colaborativo",
            "89. Compatibilidade com softwares de escritório",
            "90. Exportação em formato para impressão",
            "91. Visualização de dados em realidade aumentada (AR)",
            "92. Visualização em realidade virtual (VR)",
            "93. Narrativa de dados automatizada (data storytelling)",
            "94. Interpretação automática de gráficos",
            "95. Detecção de tendências emergentes",
            "96. Simulação de cenários (what-if analysis)",
            "97. Análise de dados em linguagem natural",
            "98. Geração de visualizações com comandos de texto",
            "99. Assistente virtual para análise de dados",
            "100. Explicabilidade dos modelos de IA (Explainable AI)"
        ],
        "BigSet": [
            "Coleta de Dados",
            "Preparação de Dados",
            "Análise Estatística",
            "Visualização",
            "Geoespacial",
            "Modelagem Preditiva",
            "Dashboards",
            "Automação",
            "Colaboração",
            "Análise Avançada"
        ],
        "Date": {
            "initial_ingress": "2025-11-12 10:22:05",
            "last_edited": "2026-02-06"
        },
        "ShortDescription": "Uma IA de Análise e Visualização de Dados é um tipo de inteligência artificial que se especializa em processar grandes volumes de dados (Big Data), identificar padrões e tendências complexas, extrair insights significativos e, crucialmente, apresentar esses insights de forma clara e compreensível através de visualizações gráficas. Ela vai além da análise estatística tradicional, utilizando algoritmos de aprendizado de máquina (Machine Learning) para automatizar e aprimorar o processo de descoberta de conhecimento nos dados.",
        "FullDescription": "Uma IA de Análise e Visualização de Dados é um tipo de inteligência artificial que se especializa em processar grandes volumes de dados (Big Data), identificar padrões e tendências complexas, extrair insights significativos e, crucialmente, apresentar esses insights de forma clara e compreensível através de visualizações gráficas.\nEla vai além da análise estatística tradicional, utilizando algoritmos de aprendizado de máquina (Machine Learning) para automatizar e aprimorar o processo de descoberta de conhecimento nos dados.\nComo funciona?\nA IA nesse contexto opera em várias camadas:\n1.\tColeta e Pré-processamento de Dados: A IA pode auxiliar na integração de dados de diversas fontes, limpeza (remoção de inconsistências, valores ausentes) e transformação (formatação para análise).\n2.\tAnálise e Descoberta de Padrões:\no\tMachine Learning (ML): Algoritmos de ML (como redes neurais, árvores de decisão, agrupamento, regressão) são aplicados aos dados para:\n\tIdentificar correlações: Descobrir relações entre diferentes variáveis.\n\tDetectar anomalias: Encontrar pontos de dados que se desviam significativamente do padrão.\n\tSegmentação: Agrupar dados com características semelhantes (ex: segmentação de clientes).\n\tPrevisão: Construir modelos para prever resultados futuros com base em dados históricos.\n\tClassificação: Categorizar dados em grupos predefinidos.\no\tProcessamento de Linguagem Natural (PLN): Se os dados forem textuais (comentários de clientes, avaliações), a IA usa PLN para extrair sentimentos, tópicos e entidades.\n3.\tGeração de Insights: Com base nas análises, a IA pode gerar insights acionáveis, como \"os clientes da faixa etária X que compraram o produto Y tendem a comprar o produto Z em seguida\", ou \"a causa principal das falhas no equipamento C é a variação de temperatura no componente B\".\n4.\tVisualização Inteligente de Dados:\no\tSugestão de Visualizações: A IA pode analisar a estrutura e o tipo dos dados e automaticamente sugerir os gráficos e tabelas mais apropriados (barras, linhas, dispersão, mapas de calor, etc.) para comunicar os insights de forma eficaz.\no\tCriação Automatizada: Algumas ferramentas podem gerar visualizações complexas com pouca intervenção humana, otimizando cores, rótulos e layouts.\no\tNarrativa de Dados: Além de gráficos, algumas IAs podem gerar descrições textuais que explicam o que os gráficos mostram e quais as implicações.\no\tDashboards Interativos: A IA pode auxiliar na criação de dashboards dinâmicos que permitem aos usuários explorar os dados e os insights em diferentes níveis de detalhe.\nBenefícios:\n•\tTomada de Decisão Aprimorada: Fornece insights mais profundos e precisos, permitindo decisões estratégicas baseadas em dados concretos.\n•\tEficiência e Automação: Reduz o tempo e o esforço manual necessários para analisar grandes volumes de dados e criar visualizações.\n•\tDescoberta de Padrões Ocultos: Capacidade de identificar correlações e anomalias que seriam invisíveis para a análise humana tradicional.\n•\tAcessibilidade: Democratiza a análise de dados, permitindo que usuários sem profundo conhecimento estatístico ou de programação possam extrair valor dos dados.\n•\tOtimização de Recursos: Ajuda empresas a identificar áreas de melhoria, otimizar processos e alocar recursos de forma mais eficiente.\n•\tPrevisão de Tendências: Capacidade de antecipar eventos futuros, como demanda de produtos, falhas de equipamentos ou comportamento do cliente.\nAplicações:\n•\tNegócios e Marketing: Análise do comportamento do cliente, otimização de campanhas, previsão de vendas, identificação de tendências de mercado.\n•\tFinanças: Detecção de fraudes, avaliação de riscos, análise de mercado, otimização de portfólios.\n•\tSaúde: Análise de dados de pacientes para diagnóstico, pesquisa de doenças, otimização de tratamentos, gestão hospitalar.\n•\tManufatura: Manutenção preditiva de máquinas, otimização de processos de produção, controle de qualidade.\n•\tLogística: Otimização de rotas, gestão de estoque, previsão de demanda de transporte.\n•\tGoverno: Análise de dados populacionais, planejamento urbano, monitoramento de segurança pública."
    },
   // continua..
]
```

trecho de `pre-selecionado.json`:

```json
[
  {
    "id": "g1",
    "FullNames": "Geração e Escrita de Textos ou Conteúdo",
    "color": "#6366f1",
    "items": [
      {
        "id": "i1",
        "name": "ChatGPT (OpenAI)"
      },
      {
        "id": "i2",
        "name": "Gemini"
      },
      {
        "id": "i4",
        "name": "Grok"
      },
      {
        "id": "i5",
        "name": "DeepSeek"
      },
      {
        "id": "i6",
        "name": "Jasper"
      }
    ]
  },
  {
    "id": "g2",
    "FullNames": "Agêntica (Agentic AI)",
    "color": "#8b5cf6",
    "items": [
      {
        "id": "i7",
        "name": "Perplexity"
      },
      {
        "id": "i8",
        "name": "Manus"
      },
      {
        "id": "i9",
        "name": "GenSpark"
      },
      {
        "id": "i10",
        "name": "Microsoft AutoGen"
      },
      {
        "id": "id905652e",
        "name": "Crew AI"
      }
    ]
  },
   // continua
]
```


--- RESPOSTA

