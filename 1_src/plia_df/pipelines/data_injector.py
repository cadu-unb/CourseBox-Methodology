"""
@file data_injector.py
@brief Pipeline de injeção de dados com controle de execução (PLIA-DF).

@details
- Usa equipe.json para controle de execução
- Respeita cache e status
- Gera apenas tarefas pendentes
- Atualiza status e rastreabilidade
"""

# /// script
# dependencies = []
# ///

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple, Any
from datetime import datetime


# =========================
# UTIL
# =========================

def load_json(path: Path) -> Any:
    """@brief Carrega JSON"""
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    """@brief Salva JSON"""
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def extract_version(file_name: str) -> Tuple[int, ...]:
    """@brief Extrai versão numérica"""
    match = re.search(r"a(\d+(?:\.\d+)*)", file_name)
    if not match:
        raise ValueError(f"Versão inválida: {file_name}")
    return tuple(map(int, match.group(1).split(".")))


def find_latest_pack(directory: Path) -> Path:
    """@brief Retorna arquivo mais recente"""
    files = list(directory.glob("packs_tasks_*.json"))
    return max(files, key=lambda f: extract_version(f.name))


def get_version_str(file_name: str) -> str:
    """@brief Retorna versão string"""
    match = re.search(r"(a\d+(?:\.\d+)*)", file_name)
    return match.group(1) if match else "unknown"


# =========================
# CORE
# =========================

def index_functional_attributes(data: List[Dict]) -> Dict[str, Dict]:
    """@brief Indexa por atributo_id"""
    return {item["atributo_id"]: item for item in data}


def build_skill_map(fa: Dict) -> Dict[str, Dict]:
    """@brief Indexa habilidades por id"""
    return {s["habilidade_id"]: s for s in fa["M10"]}


def should_process(habilidade: Dict, version: str) -> bool:
    """@brief Decide se deve processar"""
    if habilidade["status"] in ["done", "processing"]:
        return False

    # Se versão mudou, reprocessa
    if habilidade.get("version") != version:
        return True

    return habilidade["status"] == "pending"


def inject_prompt(template: str, context: Dict[str, str]) -> str:
    """@brief Injeta variáveis"""
    result = template
    for k, v in context.items():
        result = result.replace(f"{{{k}}}", v)
    return result


def update_status(
    habilidade: Dict,
    version: str,
    prompt_file: str
) -> None:
    """@brief Atualiza status e rastreabilidade"""
    habilidade["status"] = "done"
    habilidade["version"] = version
    habilidade["output"] = {
        "prompt_file": prompt_file,
        "generated_at": datetime.utcnow().isoformat()
    }


# =========================
# PIPELINE
# =========================

def process_operator(
    operador: Dict,
    pre_selected: List[Dict],
    fa_map: Dict[str, Dict],
    version: str,
    template: str,
    output_dir: Path
) -> int:
    """
    @brief Processa um operador

    @return quantidade de prompts gerados
    """
    count = 0
    output_dir.mkdir(parents=True, exist_ok=True)

    for group in operador["ferramentas"]:
        group_id = group["group_id"]

        # encontrar grupo base
        base_group = next(
            (g for g in pre_selected if g["group_id"] == group_id),
            None
        )
        if not base_group:
            continue

        for cache in group["mem"]:
            tool_id = cache["tool_id"]
            atributo_id = cache["atributo_id"]

            if atributo_id not in fa_map:
                continue

            fa = fa_map[atributo_id]
            skill_map = build_skill_map(fa)

            # encontrar ferramenta
            tool = next(
                (t for t in base_group["items"] if t["tool_id"] == tool_id),
                None
            )
            if not tool:
                continue

            for habilidade in cache["habilidades"]:
                if not should_process(habilidade, version):
                    continue

                habilidade_id = habilidade["habilidade_id"]

                if habilidade_id not in skill_map:
                    continue

                skill = skill_map[habilidade_id]

                context = {
                    "Ferramenta": tool["tool_name"],
                    "Habilidade_short": skill["title"],
                    "Habilidade_long": skill["description"],
                    "name_AtributoFuncional": fa["FullNames"],
                    "description_AtributoFuncional": fa["ShortDescription"],
                }

                prompt = inject_prompt(template, context)

                file_name = f"prompt_{count:05d}.md"
                file_path = output_dir / file_name
                file_path.write_text(prompt, encoding="utf-8")

                update_status(habilidade, version, file_name)

                count += 1

    return count


# =========================
# CLI
# =========================

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("--operator", required=True)
    parser.add_argument("--json-dir", default="3_data/0_json")
    parser.add_argument("--template", default="1_src/plia_df/prompt/roteiro.md")
    parser.add_argument("--output", default="3_data/1_raw/prompts")

    return parser.parse_args()


# =========================
# MAIN
# =========================

def main() -> None:
    args = parse_args()

    json_dir = Path(args.json_dir)
    output_dir = Path(args.output)

    equipe_path = json_dir / "equipe.json"
    pre_selected_path = json_dir / "pre-selecionado.json"

    equipe = load_json(equipe_path)
    pre_selected = load_json(pre_selected_path)

    latest_pack = find_latest_pack(json_dir)
    version = get_version_str(latest_pack.name)
    fa_data = load_json(latest_pack)

    template = Path(args.template).read_text(encoding="utf-8")

    fa_map = index_functional_attributes(fa_data)

    operador = next(
        (o for o in equipe if o["matricula"] == args.operator),
        None
    )

    if not operador:
        raise ValueError("Operador não encontrado")

    generated = process_operator(
        operador,
        pre_selected,
        fa_map,
        version,
        template,
        output_dir
    )

    # persistir equipe atualizado
    save_json(equipe_path, equipe)

    print(f"✔ {generated} prompts gerados para operador {args.operator}")


if __name__ == "__main__":
    main()