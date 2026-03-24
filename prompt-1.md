# Projeto PLIA-DF

Dando sequência nas sugestões que você me forneceu gostaria de realizar alguns cometários.

1. Não gere códigos ou qualquer outra aplicação, estamos me uma de planejamento.
2. Quando solicitado, você deve gerar código.
3. quanto ao "1.7 Template de Prompt (estrutura lógica)"
  1. Não gostei muito do resultado porque achei a sugestão de prompt pouco específica.
```prompt
CONTEXTO:
- Público: Professores do Ensino Médio (SEDF)
- Duração: 1h a 4h
- Tipo: Curso Hands-on EAD

ATRIBUTO FUNCIONAL ALVO:
{description_AtributoFuncional}

OBJETIVO DO CURSO:
Ensinar a usar {Ferramenta} para:****
→ {Habilidade_long}

TÍTULO BASE:
Já pensou utilizar o {Ferramenta} para fazer "{Habilidade_short}"?

SUBTÍTULO BASE:
Ao utilizar uma IA de {name_AtributoFuncional}...

TAREFA:
1. Gerar roteiro completo
2. Melhorar título e subtítulo
3. Garantir estrutura:
   - Introdução (com atributo funcional e o que se espera aprender);
   - 7–10 capítulos (diferentes atividade hands-on EAD);
   - Quizzes (um total de 3, com a divisão de conteúdos 1-4, 5-8 e geral);
   - Conclusão;
```

## Problemas levantados

1. Matching por `FullNames` (frágil):
Vou preferir manter a abordagem atual.

1. Explosão combinatória:
Essa é a intenção de quem solicitou a construção dessa metodologia;

## Sugestões de melhoria

1. Introduzir camada de “Curadoria Inteligente”;
Explique melhor essa sugestão, não entendi como ela se aplica a proposição desse pipeline.

2. Adicionar “nível de dificuldade”
Estamos lidando com um público muito vasto, então na etapa atual não podemos considerar conhecimento prévio.

3. Loop de Auto-Melhoria (muito forte)
Acho que essa seja sua solução para
```
Problemas levantados -> "3. Falta de controle de qualidade do output"
```
Me dê uma proposta melhor estruturado para eu entender o procedimentos sugerido.

## Retorno

- Correções de memória
- Explicações solicitadas
- Próximos passos?