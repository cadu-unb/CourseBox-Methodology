# Reformulação de Prompt

## Persona

Você é um especialista em Prompt Engineering.

## Contexto

Estou começando a desenvolver uma metodologia de construção de cursos dentro da plataforma [Coursebox.ai](https://www.coursebox.ai/). Para isso foi definido brevemente um `💼 Fluxo de Trabalho` onde explicamos brevemenete cada parte do processo. Vide trecho relacionado abaixo:

```md
O segundo momento será crucial para definir a qualidade dos resultados obtidos com o assistente de IA da plataforma [CourseBox](https://www.coursebox.ai/). A partir das transcrições, iremos construir um conjunto de **[Notas de Aula](data/processed/README.md)** com o objetivo de [roteirizar o conteúdo](0_docs/0_methodology/2_treatment/README.md) abordado de forma precisa e estruturada. Esse processo de transformação poderá ser realizado com o auxílio de ferramentas de IA (ChatGPT, Gemini, Grok, entre outras). Em seguida, inicia-se uma etapa de revisão da estrutura proposta, acompanhada do desenvolvimento manual de conceitos, exemplos e demais elementos didáticos necessários.
```

## Prompt

```md
Eu tenho uma video-aula sobre {nome_da_aula}.

Eu realizei, através do "Whisper", a transcrição dessa video-aula.

Agora preciso que você processe o arquivo transcrito em uma Apostila / Notas de aula. Foque na riqueza de detalhes, sem deixar de buscar uma estrutura robusta, organizada e didádica.

Estou anexando o arquivo "{nome_do_arquivo}.txt". A partir dele realize a tarefa mencionada.
```

# Retorno

1. SOMENTE um prompt melhorado, não precisa implementar nada.
2. Três sugestões para incluir no corpo do prompt.



----------------


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

