# 🧩 `pre-selecionado.json`

```ts
Array<Group>
Group: {
  group_id: string,
  FullNames: string,
  color: string, // hex
  items: Array<Tool>
}

Tool: {
  tool_id: string,
  tool_name: string
}
```

---

# 🧩 `packs_tasks_XXX.json`

```ts
Array<FunctionalAttribute>

FunctionalAttribute: {
  atributo_id: string,              // ex: "agentic"
  FullNames: string,                // ex: "Agêntica (Agentic AI)"
  ShortNames: string,
  M10: Array<Skill>,
  M100: Array<string>,
  BigSet: Array<string>,
  Date: {
    initial_ingress: string,        // datetime
    last_edited: string             // date
  },
  ShortDescription: string,
  FullDescription: string
}

Skill: {
  habilidade_id: string,            // ex: "M10_01"
  title: string,
  description: string
}
```

---

# 🧩 `equipe.json`

```ts
Array<Operador>

Operador: {
  matricula: string,
  nome: string,
  color: string, // hex
  ferramentas: Array<GroupRef>
}

GroupRef: {
  group_id: string,
  FullNames: string,
  color: string,
  mem: Array<Cache>
}

Cache: {
  group_id: string,
  tool_id: string,
  atributo_id: string,
  version: string,                  // ex: "a0.3"
  habilidades: Array<HabilidadeStatus>
}

HabilidadeStatus: {
  habilidade_id: string,            // ex: "M10_01"
  status: "pending" | "processing" | "done" | "error",
  output?: OutputMetadata
}

OutputMetadata: {
  prompt_file: string,              // ex: "prompt_0001.md"
  generated_at: string,             // date ou datetime
  roteiro_id?: string               // opcional (ID na plataforma)
}
```

---

# 🔗 Relações entre EDs (essencial você guardar)

```text
pre-selecionado.group_id        ↔ equipe.group_id
pre-selecionado.tool_id         ↔ equipe.tool_id
packs_tasks.atributo_id         ↔ equipe.atributo_id
packs_tasks.M10.habilidade_id   ↔ equipe.habilidade_id
packs_tasks.version             ↔ equipe.version
```

---

# 🧠 Regra de ouro (agora formalizada)

```text
IDs são SEMPRE:
- estáveis
- únicos no contexto
- usados para matching

Nomes são:
- apenas descritivos
- nunca usados como chave
```

---

# 🚀 Resultado final

```text
✔ Pipeline rastreável
✔ Cache confiável
✔ Controle por operador
✔ Base pronta para automação e dashboard
✔ Zero ambiguidade semântica
```
