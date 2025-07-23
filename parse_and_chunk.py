import fitz  # PyMuPDF
import docx
from uuid import uuid4

def parse_pdf(path):
    doc = fitz.open(path)
    chunks = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        if text.strip():
            chunks.append({
                "text": text,
                "filename": path.split("/")[-1],
                "page": page_num,
                "chunk_id": f"{path.split('/')[-1]}_p{page_num}_{uuid4().hex[:4]}"
            })
    return chunks

def parse_docx(path):
    doc = docx.Document(path)
    full_text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
    return [{
        "text": full_text,
        "filename": path.split("/")[-1],
        "page": 1,
        "chunk_id": f"{path.split('/')[-1]}_p1_{uuid4().hex[:4]}"
    }]
