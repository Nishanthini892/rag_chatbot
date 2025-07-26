import streamlit as st
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from parse_and_chunk import parse_pdf, parse_docx
from embed_and_store import embed_chunks, create_collection
import os

client = QdrantClient("http://localhost:6333")
model = SentenceTransformer("all-MiniLM-L6-v2")

create_collection()

st.title("📚 RAG Chatbot")

uploaded_file = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"])

if uploaded_file:
    file_path = os.path.join("uploaded", uploaded_file.name)
    os.makedirs("uploaded", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    if uploaded_file.name.endswith(".pdf"):
        chunks = parse_pdf(file_path)
    else:
        chunks = parse_docx(file_path)

    embed_chunks(chunks)
    st.success("✅ File processed and stored in vector database.")

query = st.text_input("Ask a question:")

if query:
    query_vector = model.encode(query).tolist()
    results = client.search(
        collection_name="rag_docs",
        query_vector=query_vector,
        limit=3
    )
    for res in results:
        st.write(f"📄 From {res.payload['filename']} (page {res.payload['page']}):")
        st.write(res.payload['text'])
