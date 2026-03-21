<!-- PATH: 0_docs/0_methodology/4_revisao.md -->
<!-- PATH: 0_docs/0_methodology/4_revisao.md -->

# 🧪 Etapa 4 — Revisão Técnica Final (QA)

---

# 🎯 Objetivo

Esta etapa garante que o curso gerado pela Coursebox.ai seja:

* **Fiel às Notas de Aula (fonte oficial)**
* **Tecnicamente correto**
* **Didaticamente consistente**

Você atua aqui como **Autor + Auditor de Qualidade (QA)**, eliminando qualquer distorção introduzida pela IA.

---

> 🚨 **Princípio-chave**
>
> A IA pode organizar conteúdo, mas não garante fidelidade.
> **A validação humana é obrigatória.**

---

# 🧭 Protocolo de Operação

A revisão deve seguir **4 camadas obrigatórias**.

---

# 🔍 1. Auditoria de Integridade

*(Gabarito vs. Entrega)*

---

## ✔ O que verificar

Compare lado a lado:

* Curso na Coursebox
* Arquivo:

```text
data/processed/aula_XX_notas_vX.md
```

---

## ✔ Validação

* Todos os tópicos foram criados?
* Todas as subseções estão presentes?
* Algum conceito foi omitido?

---

> ⚠️ **Erro Crítico**
>
> Ausência de conteúdo essencial compromete toda a aprendizagem.

---

## 🛠️ Ação corretiva

Se faltar conteúdo:

1. Copie o trecho das Notas de Aula
2. Utilize uma IA externa (ChatGPT, Gemini ou similar)
3. Gere o conteúdo estruturado
4. Cole manualmente no container correspondente na Coursebox

---

# 📏 2. Higienização de Parágrafos

*(Densidade Técnica)*

---

## ✔ O que verificar

* Parágrafos com **100–150 palavras**
* Explicações completas (não superficiais)

---

## ⚠️ Problema comum

A Coursebox tende a:

* Resumir excessivamente
* Transformar conteúdo técnico em listas rasas

---

## 🛠️ Ação corretiva

* Reescreva parágrafos curtos
* Reintroduza detalhes da transcrição original
* Garanta progressão lógica

---

> 📌 **Regra de Ouro**
>
> Se está fácil demais, provavelmente está superficial.

---

# 🧹 3. Saneamento de Alucinações e Ruídos

---

## ✔ O que verificar

* Comandos de código
* Parâmetros técnicos
* Nomes de ferramentas
* Datas e fatos históricos

---

## ⚠️ Problema crítico

A IA pode:

* Inventar funções
* Criar exemplos inexistentes
* Alterar conceitos técnicos

---

## 🛠️ Ação corretiva

* Compare com as Notas de Aula
* Delete ou corrija qualquer inconsistência

---

> 🚨 **Tolerância Zero**
>
> Conteúdo inventado não pode permanecer no curso.

---

# 🧩 4. Validação de Componentes

*(Quizzes e Imagens)*

---

## ✔ Quizzes

### Verificar:

* A pergunta faz sentido?
* A resposta correta está realmente correta?
* O nível está compatível com o conteúdo?

---

### 🛠️ Ação:

* Reescrever perguntas ambíguas
* Ajustar alternativas incorretas
* Alinhar dificuldade com o conteúdo

---

## ✔ Imagens

### Verificar:

* A imagem explica algo?
* Ou é apenas decorativa?

---

### 🛠️ Ação:

* Remover imagens irrelevantes
* Substituir por imagens mais claras (quando necessário)

---

> 📌 **Critério**
>
> Toda imagem deve ter função pedagógica.

---

# 📋 Checklist Final

Antes de concluir, valide:

* [ ] Todos os tópicos das Notas de Aula estão presentes
* [ ] Não há conteúdo inventado
* [ ] Parágrafos possuem densidade adequada
* [ ] Quizzes estão corretos e coerentes
* [ ] Imagens fazem sentido
* [ ] Fluxo do curso está lógico

---

# 📦 Resultado da Etapa

Ao final desta revisão, o curso deve estar:

* Tecnicamente correto
* Didaticamente estruturado
* Livre de alucinações

---

# 🏁 Status Final

Após concluir esta etapa, registre o curso como:

```text
Aguardando Feedback Cruzado
```

---

> 🚀 **Marco de Qualidade**
>
> Este é o ponto de transição entre a validação interna e a validação externa.

---

# ⏭️ Próxima Etapa

[`5_feedback.md`](5_feedback.md) — Auditoria Externa (Peer Review)