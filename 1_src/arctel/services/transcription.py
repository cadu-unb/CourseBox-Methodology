import whisper
import moviepy as mp # Mudança na versão 2.0+
import os

def transcrever_video_aula(nome_arquivo, pasta="videos", modelo="base"):
    # Constrói o caminho completo: "videos/Aula_20_CIRCUITOS_ELETRICOS_I.mp4"
    caminho_video = os.path.join(pasta, nome_arquivo)
    
    # Define nomes de saída baseados no vídeo
    nome_base = os.path.splitext(nome_arquivo)[0]
    caminho_audio = f"{nome_base}_temp.mp3"
    caminho_texto = f"{nome_base}_transcricao.txt"

    if not os.path.exists(caminho_video):
        print(f"Erro: O arquivo {caminho_video} não foi encontrado!")
        return

    print(f"--- Processando: {nome_arquivo} ---")

    # 1. Extração do Áudio (Nova sintaxe MoviePy)
    try:
        print("Passo 1: Extraindo áudio...")
        video = mp.VideoFileClip(caminho_video)
        video.audio.write_audiofile(caminho_audio)
        video.close()
    except Exception as e:
        print(f"Erro na extração: {e}")
        return

    # 2. Transcrição com Whisper
    try:
        print(f"Passo 2: Carregando Whisper ({modelo})...")
        model = whisper.load_model(modelo)
        
        print("Passo 3: Transcrevendo áudio (isso pode levar alguns minutos)...")
        # 'language="pt"' ajuda o modelo a focar no português desde o início
        resultado = model.transcribe(caminho_audio, fp16=False, language="pt")
        
        # 3. Salvar o arquivo final
        with open(caminho_texto, "w", encoding="utf-8") as f:
            f.write(resultado["text"])
            
        print(f"--- Concluído! ---")
        print(f"Transcrição salva em: {caminho_texto}")

    except Exception as e:
        print(f"Erro na transcrição: {e}")
    
    finally:
        if os.path.exists(caminho_audio):
            os.remove(caminho_audio)

# --- Execução ---
# transcrever_video_aula("Aula_20_CIRCUITOS_ELETRICOS_I.mp4")