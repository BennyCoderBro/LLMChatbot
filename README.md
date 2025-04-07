# LLMChatbot
Specialized in extract EDGAR finacial repots to do Q&amp;A processing by LLM
# 💼 LLM-Powered Financial Q&A System Based on SEC 10-K Reports

This project demonstrates a modular pipeline that enables **natural language financial question answering** using information extracted from public SEC EDGAR filings. The system integrates **web scraping**, **data preprocessing**, a **BERT-based answer retrieval mechanism**, and **question-type preclassification**, designed for future integration with LLM-based RAG architectures.

---

## 🎯 Project Goals

- ✅ Provide accurate, interpretable responses to financial/ESG/investor questions
- ✅ Build a real-time API layer that can integrate with frontends or agents
- ✅ Enable scalable parsing and analysis of multi-year 10-K filings
- ✅ Lay the foundation for **LLM-RAG (Retrieval-Augmented Generation)**

---

## 🛠️ Technical Stack

| Layer                  | Technology                                 |
|------------------------|---------------------------------------------|
| Web Scraping           | `requests`, `BeautifulSoup` (`bs4`)         |
| Preprocessing & Cleaning | `re`, `pandas`, HTML tag filtering         |
| Intent Classification  | Keyword-based binary classifier             |
| Text Matching Model    | `bert-large-uncased` from HuggingFace       |
| Serving / API Layer    | `Flask` (RESTful API with JSON interface)   |
| Optional Frontend      | `HTML + JS`, future: Streamlit / Vue        |
| Model Future Extensions | `sentence-transformers`, `faiss`, `OpenAI` |

---

## 🧬 Full Pipeline Overview

```text
[SEC EDGAR HTML 10-K]
      ↓
[BeautifulSoup Scraper]
      ↓
[Regex Cleaner + Section Splitter]
      ↓
[Key Paragraphs for R&D, ESG, Revenue, etc.]
      ↓
[BERT Embedding Matching]
      ↓
[Flask API → Real-time JSON Answers]
```
