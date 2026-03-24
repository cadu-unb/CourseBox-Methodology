# data_injector.py

## 🎯 Objetivo

Script responsável por gerar prompts estruturados para cursos EAD (PLIA-DF), a partir de dados JSON e um template base (`roteiro.md`).

## ⚙️ Funcionalidades

* Identifica automaticamente a versão mais recente de `packs_tasks_*.json`
* Realiza match entre:

  * `pre-selecionado.json`
  * `packs_tasks_*.json`
* Expande combinações:

  * Ferramenta × Habilidade (M10)
* Injeta os dados no template de prompt
* Gera arquivos `.md` prontos para uso em IA

## 📂 Estrutura esperada

```
3_data/
├── 0_json/
│   ├── pre-selecionado.json
│   ├── equipe.json
│   └── packs_tasks_*.json
├── 1_raw/
│   └── prompts/
```

## 🚀 Uso

### Execução padrão

```bash
python data_injector.py
```

### Argumentos disponíveis

```bash
--json-dir   Diretório dos JSONs
--template   Caminho do roteiro.md
--output     Diretório de saída dos prompts
```

## 📌 Exemplo

```bash
python data_injector.py \
  --json-dir 3_data/0_json \
  --template 1_src/plia_df/prompt/roteiro.md \
  --output 3_data/1_raw/prompts
```

## 🧠 Lógica de Versionamento

O script detecta automaticamente o arquivo mais recente:

Exemplo:

```
packs_tasks_a0.2.json
packs_tasks_a0.10.json
```

Resultado:

```
Selecionado → a0.10
```

## 🧪 Validações

* JSON válido
* Campos obrigatórios existentes
* `ShortDescription` com mínimo de 50 palavras
* Estrutura consistente entre arquivos

## ⚠️ Possíveis Erros

| Erro              | Causa                |
| ----------------- | -------------------- |
| FileNotFoundError | Arquivo ausente      |
| JSONDecodeError   | JSON malformado      |
| ValueError        | Dados inconsistentes |

## 🔄 Pipeline

```
JSON → Match → Contextos → Prompt Template → Arquivos .md
```

## 📈 Escalabilidade

O sistema suporta geração massiva de prompts, sendo adequado para:

* pipelines automatizados
* integração com APIs de IA
* geração em lote de cursos

## 🧩 Futuras Evoluções

* Filtro de curadoria
* Integração com banco de dados
* Execução distribuída
* Dashboard de monitoramento
