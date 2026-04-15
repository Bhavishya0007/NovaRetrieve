# 🌠 NovaRetrieve

**High-Velocity Document Intelligence powered by Gemini 3 Flash & FAISS.**<img width="1448" height="845" alt="Screenshot 2026-04-15 at 3 30 12 AM" src="https://github.com/user-attachments/assets/7bc7d0fc-8c87-465d-9305-e7f2b5b92cdc" />


[](https://www.python.org/downloads/)
[](https://github.com/langchain-ai/langchain)
[](https://opensource.org/licenses/MIT)

## 🚀 The Vision

**NovaRetrieve** is a minimalist, production-ready RAG (Retrieval-Augmented Generation) engine designed for sub-second document analysis. Built in 2026, it bypasses the high latency of traditional LLM pipelines by utilizing **Gemini 3 Flash-Lite** and optimized vector similarity search.

## 🛠️ Technical Architecture (2026 Stack)

  * **Engine:** `gemini-3-flash-preview` (Optimized for 1M+ token context and agentic reasoning).
  * **Vector Space:** `models/gemini-embedding-001` (3072-dimensional embeddings for superior semantic mapping).
  * **Orchestration:** `LangChain v0.4` + `langchain-community` for modular provider switching.
  * **Database:** `FAISS` (Facebook AI Similarity Search) running locally for maximum privacy and zero latency.
  * **Parser:** `pypdf` for high-fidelity extraction of structured and unstructured PDF data.

## 🏗️ How it Works

1.  **Semantic Chunking:** Documents are processed using a `RecursiveCharacterTextSplitter` with a 1000-token window, ensuring context isn't lost at the edges of paragraphs.
2.  **Vectorization:** Text is mapped into a 3072-dimensional mathematical space where similar concepts cluster together.
3.  **Neural Retrieval:** Queries are vectorized in real-time to find the "Nearest Neighbors" in the local FAISS index.
4.  **Grounded Synthesis:** Gemini 3 Flash generates answers strictly limited to the retrieved context, eliminating "hallucinations."

## 🚦 Quick Start

### 1\. Installation

```bash
git clone https://github.com/yourusername/NovaRetrieve.git
cd NovaRetrieve
python3 -m venv pdf_env
source pdf_env/bin/activate
pip3 install -r requirements.txt
```

### 2\. Configuration

Create a `.env` file:

```text
GOOGLE_API_KEY=your_key_here
```

### 3\. Launch

```bash
python3 -m streamlit run app.py
```

## 📈 Optimization Highlights

  * **Zero-Cost Inference:** Fully compatible with Google AI Studio's free tier for Gemini 3 Flash.
  * **Mac Silicon Optimized:** Leverages local `faiss-cpu` for instant search on macOS.
  * **Dependency Resolution:** Architected to handle the modern `protobuf 6.x` and `pydantic v2` ecosystem.
