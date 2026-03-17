#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""!
@file text_extractor.py
@brief Pipeline robusto para extração de texto de PDFs digitais e digitalizados.

Este módulo implementa um pipeline híbrido de extração de texto que tenta
primeiro a extração nativa de PDFs e utiliza OCR automaticamente quando
necessário.

Principais funcionalidades:
- Segmentação seletiva de páginas
- Extração preservando layout lógico
- Fallback automático para OCR
- Persistência em UTF-8

Dependências principais:
- PyMuPDF (fitz)
- pytesseract
- Pillow

@author
Carlos Eduardo Papa

@date
2026
"""

import os
import re
from typing import List, Optional

import fitz  # PyMuPDF
import pytesseract
from PIL import Image


MIN_CHARS_THRESHOLD = 30


class PDFTextExtractor:
    """!
    @class PDFTextExtractor
    @brief Classe responsável pela extração híbrida de texto em PDFs.
    """

    def __init__(self, pdf_path: str) -> None:
        """!
        @brief Inicializa o extrator.

        @param pdf_path Caminho para o arquivo PDF.

        @throws FileNotFoundError Caso o arquivo não exista.
        @throws RuntimeError Caso o PDF não possa ser aberto.
        """

        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {pdf_path}")

        self.pdf_path = pdf_path

        try:
            self.doc = fitz.open(pdf_path)
        except Exception as exc:
            raise RuntimeError(f"Erro ao abrir PDF: {exc}") from exc

    @staticmethod
    def parse_page_selection(selection: str) -> List[int]:
        """!
        @brief Converte string de seleção de páginas em lista de índices.

        Exemplo:
        "1,5,10-12" -> [1,5,10,11,12]

        @param selection String com páginas selecionadas.
        @return Lista de páginas (base 1).
        """

        pages = []

        parts = selection.split(",")

        for part in parts:
            part = part.strip()

            if "-" in part:
                start, end = part.split("-")
                pages.extend(range(int(start), int(end) + 1))
            else:
                pages.append(int(part))

        return sorted(set(pages))

    @staticmethod
    def _validate_text_density(text: str) -> bool:
        """!
        @brief Verifica se a extração nativa retornou texto suficiente.

        @param text Texto extraído.
        @return True se o texto for considerado válido.
        """

        clean_text = re.sub(r"\s+", "", text)

        return len(clean_text) >= MIN_CHARS_THRESHOLD

    @staticmethod
    def _extract_structured_text(page: fitz.Page) -> str:
        """!
        @brief Extrai texto preservando layout lógico.

        Utiliza blocos de texto para evitar mistura de colunas
        ou regiões distintas da página.

        @param page Página do PDF.
        @return Texto estruturado extraído.
        """

        blocks = page.get_text("blocks")

        blocks_sorted = sorted(blocks, key=lambda b: (b[1], b[0]))

        text_parts = []

        for block in blocks_sorted:
            block_text = block[4].strip()
            if block_text:
                text_parts.append(block_text)

        return "\n".join(text_parts)

    @staticmethod
    def _perform_ocr(page: fitz.Page) -> str:
        """!
        @brief Executa OCR em uma página do PDF.

        @param page Página do PDF.
        @return Texto extraído via OCR.
        """

        pix = page.get_pixmap(dpi=300)

        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        text = pytesseract.image_to_string(image, lang="por+eng")

        return text

    def extract_pages(self, pages: Optional[List[int]] = None) -> str:
        """!
        @brief Executa extração de texto nas páginas especificadas.

        @param pages Lista de páginas (base 1). Se None, processa todas.
        @return Texto consolidado extraído do documento.
        """

        extracted_text = []

        if pages is None:
            pages = list(range(1, len(self.doc) + 1))

        for page_number in pages:

            try:
                page = self.doc.load_page(page_number - 1)

                text = self._extract_structured_text(page)

                if not self._validate_text_density(text):
                    text = self._perform_ocr(page)

                extracted_text.append(
                    f"\n===== Página {page_number} =====\n{text}"
                )

            except Exception as exc:
                extracted_text.append(
                    f"\n===== Página {page_number} =====\n"
                    f"[ERRO NA EXTRAÇÃO]: {exc}"
                )

        return "\n".join(extracted_text)

    def save_to_txt(self, text: str, output_path: str) -> None:
        """!
        @brief Salva texto consolidado em arquivo UTF-8.

        @param text Texto a ser salvo.
        @param output_path Caminho do arquivo de saída.
        """

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)


def extract_pdf_text(
    pdf_path: str,
    output_txt: str,
    page_selection: Optional[str] = None
) -> None:
    """!
    @brief Função utilitária de alto nível para extração completa.

    @param pdf_path Caminho do PDF.
    @param output_txt Caminho do TXT de saída.
    @param page_selection Intervalo de páginas (ex: "1,5,10-12").
    """

    extractor = PDFTextExtractor(pdf_path)

    pages = None

    if page_selection:
        pages = extractor.parse_page_selection(page_selection)

    text = extractor.extract_pages(pages)

    extractor.save_to_txt(text, output_txt)


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="Pipeline híbrido de extração de texto em PDFs."
    )

    parser.add_argument("pdf", help="Caminho do arquivo PDF")
    parser.add_argument("output", help="Arquivo TXT de saída")
    parser.add_argument(
        "--pages",
        help="Intervalo de páginas (ex: 1,5,10-12)",
        default=None
    )

    args = parser.parse_args()

    extract_pdf_text(args.pdf, args.output, args.pages)