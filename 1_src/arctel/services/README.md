<!-- PATH: 1_src/services/README.md -->
# 🧩 Services Layer

## 📌 Objetivo
Camada responsável pela lógica de negócio e processamento de dados.

---

## 🔧 Serviços Disponíveis

### 📄 PDF Text Extractor
Pipeline híbrido para extração de texto de PDFs.

👉 [Documentação completa](text_extractor.md)

---

### 🎧 Video Transcription
Pipeline de transcrição de vídeos com Whisper.

👉 [Documentação completa](transcription.md)

---

## 📏 Regras Arquiteturais

- Serviços devem ser desacoplados
- Não depender diretamente de pipelines
- Devem ser reutilizáveis e testáveis