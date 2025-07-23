
# Local RAG Chatbot 

This project is a lightweight, local Retrieval-Augmented Generation (RAG) chatbot that answers questions based on uploaded PDF documents. It is built using pure Python without using LangChain. The app uses Qdrant for vector search and Streamlit for the web interface.
##  Features

- Upload a PDF and ask questions related to its content
- Uses sentence-transformers for embeddings
- Uses Qdrant as a local vector store
- Minimalistic and beginner-friendly design
- Streamlit UI to ask questions and display answers
- No external APIs or LangChain required!

---

## Requirements

- Python 3.9+
- Docker (for running Qdrant locally)
- The following Python packages (see `requirements.txt`):
  - streamlit
  - sentence-transformers
  - PyMuPDF (fitz)
  - qdrant-client

---

## Project Structure

```
📦rag_chatbot
├── app.py              
├── embed_and_store.py 
├── parse_and_chunk.py  
├── requirements.txt    

 How to Run

### 1. Start Qdrant using Docker

```bash
docker run -p 6333:6333 qdrant/qdrant
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

## How It Works

1. Upload a PDF file in the Streamlit app
2. The content is split into smaller chunks
3. Each chunk is converted to vector embeddings
4. Qdrant stores the vectors locally
5. When you ask a question, the app finds the most relevant chunks
6. It uses a local model to generate answers based only on those chunks — not the entire content

##  Notes

- Make sure Docker is running before you start the app.
- You can modify the logic in `app.py` to change the question-answering behavior.
- This project does not require internet after models are downloaded.

##  OUTPUT LINK:
https://drive.google.com/file/d/1BWNKWJvJC4veJpWTfGyRxocRueNHGWEv/view?usp=sharing


##  Credits

Built By
NISHANTHINI S
NIKSHITHA H
      — inspired by open-source RAG research.
