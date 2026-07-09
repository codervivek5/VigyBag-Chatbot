# VigyBag RAG Chatbot

## Project Overview

VigyBag RAG Chatbot is an AI-powered FAQ assistant built for the VigyBag e-commerce platform.

The chatbot uses Retrieval-Augmented Generation (RAG) to answer user questions using FAQ data stored in a vector database.

---

## Features

* FAQ-based question answering
* Semantic search using embeddings
* ChromaDB vector database
* Gemini 2.5 Flash integration
* Function-based architecture
* Modular project structure

---

## Tech Stack

* Python
* ChromaDB
* Sentence Transformers
* Gemini 2.5 Flash
* dotenv

---

## Project Structure

```text
ChatBot/
│
├── data/
│   └── faq.json
│
├── vectorstore/git 
│   └── chroma_db/
│
├── loader.py
├── chunking.py
├── embeddings.py
├── ingest.py
├── retriever.py
├── prompt.py
├── llm.py
├── rag_pipeline.py
├── main.py
├── config.py
├── requirements.txt
└── README.md
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Run the Project

Create embeddings and store them in ChromaDB:

```bash
python ingest.py
```

Start the chatbot:

```bash
python main.py
```

---

## Example

```text
You: What is VigyBag?

Bot: VigyBag is an eco-friendly e-commerce platform that offers sustainable and handcrafted products while supporting rural artisans and women entrepreneurs.
```

---

## Future Enhancements

* FastAPI Integration
* PostgreSQL Chat History
* Authentication
* Admin Dashboard
* Product Recommendation System
* Conversation Memory

```
```
