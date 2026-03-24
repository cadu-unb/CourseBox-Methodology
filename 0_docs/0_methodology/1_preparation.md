<!-- PATH: 0_docs/0_methodology/1_preparation.md -->

# ⚠️ Etapa 1 — Elaboração (PLIA-DF)

## 🎯 Objetivo da Etapa

Gerar roteiros de cursos EAD (hands-on) a partir de dados estruturados, utilizando IA e o pipeline PLIA-DF.

## 📥 Entradas Necessárias

Antes de iniciar, certifique-se de que os seguintes arquivos estão disponíveis:

### 📁 Dados estruturados

```
3_data/0_json/
├── pre-selecionado.json
├── packs_tasks_*.json
└── equipe.json
```

> O sistema utilizará automaticamente a versão mais recente de `packs_tasks_*.json`.

### 🧾 Template de Prompt

```
1_src/plia_df/prompt/roteiro.md
```

## ⚙️ Execução do Pipeline

Execute o script responsável pela geração dos prompts:

```bash
python data_injector.py --operator <matricula>
```

### 🔍 O que o script faz:

* Identifica a versão mais recente dos dados (`packs_tasks`)
* Filtra as ferramentas atribuídas ao operador
* Verifica o estado de execução (`pending`, `done`, etc.)
* Gera apenas os prompts ainda não processados
* Atualiza automaticamente o controle de execução em `equipe.json`

## 📤 Saídas Geradas

Os prompts serão gerados em:

```
3_data/1_raw/prompts/
```

Exemplo:

```
prompt_00001.md  
prompt_00002.md  
...
```

Cada arquivo representa um contexto específico de:

```
Ferramenta × Habilidade × Atributo Funcional
```

## 🤖 Geração dos Roteiros (IA)

Para cada prompt gerado:

1. Copie o conteúdo do arquivo `.md`
2. Cole na plataforma de IA definida
3. Gere o roteiro do curso

## 🔍 Validação Inicial

Após gerar o roteiro, verifique rapidamente:

```
- O roteiro foi gerado corretamente?
- Possui introdução?
- Contém entre 7 e 10 capítulos?
- Inclui quizzes?
```

> Caso algum item falhe, refaça a geração antes de prosseguir.

## ⚠️ Tratamento de Erros

Se ocorrerem problemas:

### ❌ Prompt não gerado

* Verifique se há tarefas com status `pending` no `equipe.json`

### ❌ Erro ao executar o script

* Validar estrutura dos arquivos JSON
* Confirmar existência dos caminhos

### ❌ Resposta ruim da IA

* Reexecutar o prompt
* Ajustar manualmente, se necessário

## 📌 Boas Práticas

* Execute o pipeline por operador (evite execução massiva descontrolada)
* Revise rapidamente os prompts antes de enviar à IA
* Mantenha organização dos arquivos gerados
* Não altere manualmente o `equipe.json` durante execução

## 🔄 Saída da Etapa

Ao final desta etapa, espera-se:

```
→ Conjunto de roteiros de cursos gerados pela IA  
→ Rastreáveis e vinculados aos prompts gerados  
→ Prontos para a etapa "Operação"  
```

## 🚨 Ponto de Atenção

Este processo assume que o operador sabe utilizar uma plataforma de IA.

Caso necessário, padronize previamente a ferramenta (ex: ChatGPT, Gemini, etc.).

# ⏭️ Próxima Etapa

[`3_operation.md`](3_operation.md) — Lidando com a plataforma CourseBox.ai.
