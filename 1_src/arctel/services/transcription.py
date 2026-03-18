#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""!
@file transcription.py
@brief Pipeline de transcrição automática de vídeos utilizando Whisper.

Este módulo implementa um pipeline robusto para:
- Extração de áudio de vídeos
- Transcrição com Whisper
- Persistência em arquivo TXT (UTF-8)

Principais funcionalidades:
- Uso de pathlib para manipulação de caminhos
- Arquitetura modular
- Tratamento de exceções
- CLI para execução direta

Dependências:
- openai-whisper
- moviepy

@author
Carlos Eduardo Papa

@date
2026
"""

from pathlib import Path
from typing import Optional

import whisper
import moviepy as mp


class VideoTranscriber:
    """!
    @class VideoTranscriber
    @brief Classe responsável pela transcrição de vídeos.
    """

    def __init__(self, model_name: str = "base") -> None:
        """!
        @brief Inicializa o transcritor com modelo Whisper.

        @param model_name Nome do modelo Whisper (tiny, base, small, medium, large).
        """

        self.model_name = model_name
        self.model = self._load_model()

    def _load_model(self) -> whisper.Whisper:
        """!
        @brief Carrega o modelo Whisper.

        @return Instância do modelo Whisper carregado.
        """

        return whisper.load_model(self.model_name)

    @staticmethod
    def _validate_video_path(video_path: Path) -> None:
        """!
        @brief Valida existência do arquivo de vídeo.

        @param video_path Caminho do vídeo.
        @throws FileNotFoundError Caso o arquivo não exista.
        """

        if not video_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {video_path}")

    @staticmethod
    def _extract_audio(video_path: Path, output_audio: Path) -> None:
        """!
        @brief Extrai áudio de um arquivo de vídeo.

        @param video_path Caminho do vídeo.
        @param output_audio Caminho do arquivo de áudio temporário.
        @throws RuntimeError Caso ocorra falha na extração.
        """

        try:
            video = mp.VideoFileClip(str(video_path))

            if video.audio is None:
                raise RuntimeError("O vídeo não possui trilha de áudio.")

            video.audio.write_audiofile(str(output_audio))
            video.close()

        except Exception as exc:
            raise RuntimeError(f"Erro na extração de áudio: {exc}") from exc

    def _transcribe_audio(self, audio_path: Path) -> str:
        """!
        @brief Executa a transcrição do áudio.

        @param audio_path Caminho do arquivo de áudio.
        @return Texto transcrito.
        """

        result = self.model.transcribe(
            str(audio_path),
            fp16=False,
            language="pt"
        )

        return result.get("text", "").strip()

    @staticmethod
    def _save_transcription(text: str, output_path: Path) -> None:
        """!
        @brief Salva a transcrição em arquivo TXT.

        @param text Texto transcrito.
        @param output_path Caminho do arquivo de saída.
        """

        output_path.write_text(text, encoding="utf-8")

    def transcribe(
        self,
        video_path: Path,
        output_dir: Optional[Path] = None
    ) -> Path:
        """!
        @brief Executa pipeline completo de transcrição.

        @param video_path Caminho do arquivo de vídeo.
        @param output_dir Diretório de saída (opcional).
        @return Caminho do arquivo de transcrição gerado.
        """

        self._validate_video_path(video_path)

        if output_dir is None:
            output_dir = video_path.parent

        output_dir.mkdir(parents=True, exist_ok=True)

        base_name = video_path.stem

        audio_path = output_dir / f"{base_name}_temp.mp3"
        output_text = output_dir / f"{base_name}_transcricao.txt"

        try:
            print(f"[INFO] Processando: {video_path.name}")

            print("[INFO] Extraindo áudio...")
            self._extract_audio(video_path, audio_path)

            print("[INFO] Transcrevendo áudio...")
            text = self._transcribe_audio(audio_path)

            print("[INFO] Salvando transcrição...")
            self._save_transcription(text, output_text)

            print(f"[SUCCESS] Transcrição salva em: {output_text}")

            return output_text

        finally:
            if audio_path.exists():
                audio_path.unlink()


def transcribe_video(
    video_path: str,
    model: str = "base",
    output_dir: Optional[str] = None
) -> None:
    """!
    @brief Função utilitária para transcrição de vídeo.

    @param video_path Caminho do vídeo.
    @param model Nome do modelo Whisper.
    @param output_dir Diretório de saída (opcional).
    """

    transcriber = VideoTranscriber(model)

    video_path_obj = Path(video_path)

    output_dir_obj = Path(output_dir) if output_dir else None

    transcriber.transcribe(video_path_obj, output_dir_obj)


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="Pipeline de transcrição de vídeos com Whisper."
    )

    parser.add_argument("video", help="Caminho do arquivo de vídeo")
    parser.add_argument(
        "--model",
        default="base",
        help="Modelo Whisper (tiny, base, small, medium, large)"
    )
    parser.add_argument(
        "--output",
        help="Diretório de saída",
        default=None
    )

    args = parser.parse_args()

    transcribe_video(
        video_path=args.video,
        model=args.model,
        output_dir=args.output
    )