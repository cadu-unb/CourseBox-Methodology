import subprocess
from pathlib import Path


def generate_docs() -> None:
    """!
    @brief Localiza o Doxyfile via caminho absoluto e invoca o Doxygen.
    @details Resolve o caminho independentemente de onde o script é executado.
    """
    script_path  = Path(__file__).resolve()
    project_root = script_path.parents[2]
    doxyfile     = project_root / "1_src" / "Doxyfile"
    workdir      = doxyfile.parent

    if not doxyfile.exists():
        print(f"[!] Doxyfile não encontrado em: {doxyfile}")
        return

    print(f"[*] Gerando documentação a partir de: {workdir}")

    try:
        result = subprocess.run(
            ["doxygen", str(doxyfile)],
            cwd=str(workdir),
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("[V] Documentação gerada com sucesso.")
            print(f"[i] Saída em: {workdir / 'html' / 'index.html'}")
        else:
            print("[!] Doxygen reportou erros:")
            print(result.stderr)
    except FileNotFoundError:
        print("[!] Doxygen não encontrado. Instale em: https://www.doxygen.nl/download.html")


if __name__ == "__main__":
    generate_docs()