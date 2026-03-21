<!-- PATH: 0_docs/0_methodology/6_improvement.md -->

<!-- PATH: 0_docs/0_methodology/6_improvement.md -->

# 🔧 Etapa 6 — Apuração e Melhoria Contínua
;
# 🎯 Objetivo

Nesta etapa, o autor realiza a **implementação sistemática das melhorias** com base no feedback recebido em `5_feedback.md`.

O foco é:

* Corrigir falhas críticas
* Refinar a qualidade pedagógica
* Preparar o curso para validação final
;
> 🚨 **Princípio-chave**
>
> Feedback não é opinião — é insumo de melhoria.
> O valor está na **execução disciplinada das correções**.
;
# 🧭 1. Triagem de Feedback

Antes de corrigir, classifique cada item do feedback.
;
## 🔴 Críticas Técnicas *(Ação Obrigatória)*

Incluem:

* Alucinações da IA
* Conceitos incorretos
* Informações não presentes nas Notas de Aula
;
### ✔ Ação

* Corrigir imediatamente
* Validar com o material original (`data/processed/`)
;
> ⚠️ **Tolerância Zero**
>
> Nenhum conteúdo inventado pode permanecer no curso.
;
## 🟡 Sugestões de UX / Fluidez *(Ação de Refino)*

Incluem:

* Texto confuso
* Explicações superficiais
* Falta de exemplos
;
### ✔ Ação

* Melhorar clareza
* Expandir explicações
* Ajustar progressão didática
;
## 🔵 Sugestões Estéticas *(Ação Opcional — Fase 3)*

Incluem:

* Imagens decorativas
* Ajustes visuais
* Layout
;
### ✔ Ação

* Registrar para melhoria futura
* Não priorizar nesta fase
;
# 🤖 2. Ciclo de Correção via IA

Utilize o feedback como insumo direto para geração de conteúdo corrigido.
;
## 🔁 Processo

1. Identifique o problema no `5_feedback.md`
2. Localize o trecho correspondente nas Notas de Aula
3. Construa um prompt de correção
4. Utilize IA externa (ChatGPT, Gemini, etc.)
5. Gere nova versão do conteúdo
;
## 🧾 Exemplo de Prompt de Correção

```text
Você é um Designer Instrucional.

O seguinte trecho de um curso está superficial:
{colar conteúdo atual}

O feedback recebido foi:
"O conteúdo está raso e não explica o conceito adequadamente."

Com base no trecho original das Notas de Aula abaixo:
{colar trecho da nota de aula}

Reescreva o conteúdo com maior densidade técnica, clareza e progressão didática.
```
;
> 📌 **Boas práticas**
>
> * Sempre usar o material original como base
> * Nunca pedir para a IA "inventar" conteúdo
> * Priorizar fidelidade sobre criatividade
;
# ⚙️ 3. Protocolo de Atualização na Coursebox

Após gerar o conteúdo corrigido:
;
## ✔ Substituição de conteúdo

1. Acesse a lição correspondente
2. Localize o container (bloco de conteúdo)
3. Substitua o texto antigo pelo novo
4. Salve as alterações
;
## 🔍 Verificação de impacto

Após cada correção, valide:

* A próxima lição ainda faz sentido?
* Há referências quebradas?
* O fluxo lógico foi mantido?
;
> ⚠️ **Atenção**
>
> Correções locais podem gerar inconsistências globais.
;
# ⚖️ 4. Resolução de Conflitos

Nem todo feedback deve ser aceito automaticamente.
;
## ✔ Quando houver discordância

Avalie com base em:

1. **Notas de Aula (fonte oficial)**
2. **Objetivo pedagógico do curso**
3. **Coerência global**
;
## 🧠 Critério de decisão

* Se o feedback melhora a fidelidade → **Aceitar**
* Se melhora a clareza sem distorcer → **Aceitar**
* Se contradiz a fonte original → **Rejeitar**
;
## 🛠️ Ação

* Documentar a decisão
* Justificar tecnicamente
;
# 📊 Log de Implementação

Registre todas as ações realizadas:
;
```md id="log-implementacao"
| ID | Localização | Tipo de Feedback | Ação | Status | Observação |
|----|------------|------------------|------|--------|-----------|
| 01 | Módulo 1 / Lição 2 | Crítica Técnica | Corrigido conteúdo | ✔ | Ajustado conforme Notas |
| 02 | Módulo 2 / Lição 1 | UX | Expandido parágrafo | ✔ | Melhorado exemplo |
| 03 | Módulo 3 / Lição 4 | Estética | Adiado | ⏳ | Fase 3 |
```
;
> 📌 **Nota**
>
> O log garante rastreabilidade e transparência no processo.
;
# 🚨 Alerta de Qualidade

Antes de finalizar, valide:

* [ ] Todas as críticas técnicas foram corrigidas
* [ ] Não há alucinações remanescentes
* [ ] O conteúdo está mais claro que a versão anterior
* [ ] O fluxo do curso permanece coerente
;
> 🚨 **Erro Crítico**
>
> Se ainda houver conteúdo não rastreável nas Notas de Aula, a etapa NÃO está concluída.
;
# 📦 Resultado da Etapa

Ao final, você terá:

* Curso corrigido e refinado
* Feedback devidamente tratado
* Base sólida para finalização
;
# ⏭️ Próxima Etapa

[`7_customization.md`](7_customization.md) — Personalização e Refinamento Final
