from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

client = QdrantClient("http://localhost:6333")
model = SentenceTransformer("all-MiniLM-L6-v2")

def create_collection():
    client.recreate_collection(
        collection_name="rag_docs",
        vectors_config=VectorParams(size=384, distance=Distance.COSINE)
    )

def embed_chunks(chunks):
    texts = [chunk['text'] for chunk in chunks]
    embeddings = model.encode(texts).tolist()
    points = [
        PointStruct(id=i, vector=embeddings[i], payload=chunks[i])
        for i in range(len(chunks))
    ]
    client.upload_points(collection_name="rag_docs", points=points)
