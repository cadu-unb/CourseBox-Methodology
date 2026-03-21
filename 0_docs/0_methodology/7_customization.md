<!-- PATH: 0_docs/0_methodology/7_customization.md -->

# 🎨 Etapa 7 — Personalização Estética (Fase 3)

# 🎯 Objetivo

Nesta etapa, o curso deixa de ser apenas **correto** e passa a ser **memorável**.

O foco é transformar o conteúdo em uma experiência visual:

* Mais profissional
* Mais engajadora
* Mais coerente com a identidade do projeto

> 🚀 **Princípio-chave**
>
> Não buscamos perfeição em código.
> Buscamos **consistência visual e clareza pedagógica**.

# 🧩 1. O Recurso "Embutir Código"

Para aplicar personalizações, utilize o botão:

<!-- Ilustração - print da tela -->
<div align="center">
 <img src="images/7-1_botao.png" width="300px" />
</div


## 🔧 O que ele faz?

O recurso **"Embutir Código"** permite inserir:

* HTML
* CSS inline (dentro das tags)

Na prática, você estará:

> 💡 **Injetando um layout customizado diretamente no conteúdo da aula**

> ⚠️ **Atenção**
>
> Qualquer erro no código pode quebrar a renderização da página.

# 🧠 2. Filosofia "No-Punishment"

Você **não precisa ser desenvolvedor front-end** para executar esta etapa.

## ✔ Regra de Ouro

Use IA como copiloto:

* ChatGPT
* Gemini
* Grok

## 🎯 Foco

* Manter **padrão visual consistente**
* Reutilizar templates
* Evitar "inventar do zero"

> 📌 **Mentalidade correta**
>
> Você não escreve código — você **orquestra código com IA**.

# 🧬 3. Anatomia do Template

Abaixo está o **Template Base oficial** (referência obrigatória):

## 🧾 Template Base

```html
<br><div style="max-width:900px;margin:0 auto;padding:40px 20px">

    <div style="background-color:#234375;color:white;padding:30px;border-radius:8px 8px 0 0;box-shadow:0 2px 8px rgba(0,0,0,0.1)">
        <h1 style="margin:0;color:white;font-size:2.2em;font-weight:600">Título da Aula</h1>
        <p style="margin:10px 0 0 0;font-size:1.1em;opacity:0.95">Subtítulo / Seção</p>
    </div>

    <div style="background-color:white;padding:40px;box-shadow:0 2px 8px rgba(0,0,0,0.1)">

        <div style="background-color:#f1f1f1;padding:20px;border-radius:6px;margin:25px 0;border-left:5px solid #2C77E8;text-align:center;font-style:italic;color:#002868;font-size:1.05em">
            Destaque / Insight / "Pulo do Gato"
        </div>

        <p style="color:#212E42;font-size:1.05em;margin-bottom:30px;text-align:justify">
            Conteúdo principal da aula...
        </p>

    </div>
</div>
```

## 🧱 Componentes

### 🔵 Header

* Cor principal: `#234375`
* Contém:

  * Título
  * Subtítulo

✔ Função: **Contextualizar rapidamente o aluno**

### ⚪ Body

* Fundo branco
* Espaçamento interno (padding)
* Texto justificado

✔ Função: **Garantir legibilidade**

### 🟦 Box de Destaque

* Fundo cinza claro
* Borda lateral azul (`#2C77E8`)
* Texto em itálico

✔ Função: destacar:

* Insights
* Resumos
* Dicas importantes

> 📌 **Boa prática**
>
> Use no máximo 1–2 caixas de destaque por página.

# 🤖 4. Fluxo de Trabalho com IA

## 🔁 Processo

1. Copie o **Template Base**
2. Separe o texto da aula
3. Envie para a IA com instruções claras

## 🧾 Prompt recomendado

```text
Aja como um desenvolvedor Front-end.

Insira o conteúdo abaixo dentro deste template HTML, mantendo as cores #234375 e #2C77E8.

Conteúdo:
{colar texto da aula}

Template:
{colar template base}

Regras:
- Não remover nenhuma div
- Manter estrutura intacta
- Substituir apenas textos
```

## ✔ Resultado esperado

* HTML pronto para colar na Coursebox
* Estrutura preservada
* Conteúdo organizado

> ⚠️ **Erro comum**
>
> Pedir para a IA "melhorar o layout" → isso quebra o padrão visual.

# 🧪 5. Teste de Visualização

Antes de aplicar em larga escala:

## ✔ Procedimento

1. Crie uma aula ou bloco vazio
2. Clique em **"Embutir Código"**
3. Cole o HTML gerado
4. Salve

## 🔍 Verificações

* O layout carregou corretamente?
* Há espaçamento adequado?
* O texto está legível?

## 📱 Teste de Responsividade

Simule:

* Desktop
* Tablet
* Mobile

> ⚠️ **Atenção**
>
> Evite larguras fixas quebradas — use sempre:
>
> ```html
> max-width:900px;
> margin:0 auto;
> ```

# 🚨 Erros Críticos Comuns

## ❌ Tags não fechadas

Exemplo de erro:

```html
<div>
    <p>Texto
```

✔ Correto:

```html
<div>
    <p>Texto</p>
</div>
```

## ❌ Alterar estrutura do template

* Remover `<div>`
* Alterar cores padrão
* Inserir estilos conflitantes

> 🚨 **Regra absoluta**
>
> Nunca modifique a estrutura base.
> Apenas substitua conteúdo.

# 🔎 Material Suplementar

▶️ [YouTube](https://youtu.be/99QXkotCS-Q)

# 📦 Resultado da Etapa

Ao final, você terá:

* Curso visualmente consistente
* Identidade profissional
* Melhor experiência de leitura

# 🏁 Conclusão da Metodologia

Com esta etapa, a metodologia **Arctel** atinge seu ciclo completo:

1. Separação
2. Tratamento
3. Operação
4. Revisão
5. Feedback
6. Melhoria
7. Personalização

> 🚀 **Entrega Final**
>
> Um curso:
>
> * Tecnicamente correto
> * Didaticamente estruturado
> * Visualmente profissional

**Status Final:** ✅ Pronto para Publicação
