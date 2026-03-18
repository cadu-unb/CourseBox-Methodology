<!-- PATH: 0_docs/0_methodology/5_feedback.md -->

# 🔍 Etapa 5 — Auditoria de Experiência e Integridade

---

# 🎯 Objetivo

Esta etapa consiste na **revisão externa (peer review)** do curso gerado na plataforma Coursebox.ai, com foco em identificar falhas que passaram despercebidas pelo autor original.

O revisor atua como **proxy do aluno final**, validando:

* Fidelidade técnica (comparação com as Notas de Aula)
* Coerência pedagógica
* Qualidade da experiência de navegação
* Integridade dos elementos do curso

---

> 🚨 **Princípio-chave**
>
> Se o revisor não compreende claramente um conceito, o aluno final também não compreenderá.

---

# 🧭 Escopo da Auditoria

Durante a navegação completa no curso, você deve avaliar os seguintes eixos:

---

## 🧠 1. Identificação de Alucinações

Verifique se a IA introduziu:

* Conceitos não presentes nas Notas de Aula
* Dados técnicos incorretos
* Datas, nomes ou definições inexistentes

---

### ✔ Como validar

* Compare diretamente com:

```text
data/processed/aula_XX_notas_vX.md
```

---

> ⚠️ **Erro Crítico**
>
> Qualquer conteúdo inventado ou tecnicamente incorreto deve ser tratado como prioridade máxima.

---

## 🔗 2. Inconsistência Pedagógica

Avalie a progressão do conteúdo:

* Há saltos lógicos entre páginas?
* Conceitos são introduzidos antes de serem explicados?
* Os quizzes refletem o conteúdo apresentado?

---

### ✔ Pontos de atenção

* Perguntas mais difíceis que o conteúdo base
* Falta de exemplos antes de avaliações
* Sequência didática quebrada

---

## 🖼️ 3. Qualidade dos Ativos

### Imagens

* São relevantes ou apenas decorativas?
* Ajudam a explicar ou confundem?

---

### Layout (Containers)

* Facilitam a leitura?
* Existe poluição visual?
* Há excesso de blocos ou elementos desnecessários?

---

> 📌 **Sugestão Estética**
>
> Problemas visuais não bloqueiam o curso, mas impactam diretamente o engajamento.

---

## ⚙️ 4. Erros de Fluxo

Verifique:

* Links quebrados
* Páginas vazias
* Vídeos que não carregam
* Elementos interativos não funcionais

---

> ⚠️ **Erro Crítico**
>
> Qualquer falha que impeça o avanço do aluno no curso deve ser corrigida imediatamente.

---

# 📝 Protocolo de Registro

Todos os problemas identificados devem ser registrados no formato abaixo:

---

## 📌 Modelo de Registro

```md
### 🔴 [Erro Crítico] ou 🟡 [Sugestão]

- **Localização:** Módulo X / Lição Y  
- **Tipo de Falha:** Alucinação | Erro Técnico | UX | Estética  
- **Descrição:**  
Descreva claramente o problema encontrado.  
Se aplicável, cite o trecho correto presente nas Notas de Aula.

- **Sugestão de Ajuste:**  
Indique como corrigir o problema.  
Exemplo: "Refazer o prompt do tópico utilizando o conteúdo do parágrafo X da aula_02_notas_v1.md"
```

---

# 📊 Critérios de Classificação

## 🔴 Erro Crítico

Impacta diretamente:

* A veracidade do conteúdo
* A compreensão do aluno
* A navegabilidade do curso

**Exemplos:**

* Conceito errado
* Informação inventada
* Link quebrado essencial

---

## 🟡 Sugestão de Melhoria

Impacta:

* Clareza
* Engajamento
* Estética

**Exemplos:**

* Imagem pouco relevante
* Texto confuso, mas correto
* Layout poluído

---

# 🧪 Procedimento de Auditoria

1. Acesse o curso completo na Coursebox
2. Navegue **do início ao fim**
3. Compare com as Notas de Aula
4. Registre todos os problemas encontrados
5. Classifique corretamente cada item

---

> ⚠️ **Disciplina Operacional**
>
> Não confie na memória.
> Sempre valide com o arquivo de referência.

---

# 📦 Resultado Esperado

Ao final desta etapa, você deve entregar:

* Um relatório estruturado
* Lista clara de erros e melhorias
* Recomendações acionáveis para o autor

---

# 🚀 Impacto da Etapa

Esta fase é responsável por garantir:

* Qualidade técnica do curso
* Experiência consistente para o aluno
* Redução de retrabalho nas etapas finais

---

# ⏭️ Próxima Etapa

[`6_improvement.md`](6_improvement.md) — Implementação das Correções
