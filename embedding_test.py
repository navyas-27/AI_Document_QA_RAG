from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer

# Read the PDF
reader = PdfReader("Model Ans Odd 2024.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"


# Create chunks
chunk_size = 300

chunks = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    chunks.append(chunk)


# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Create embeddings for all chunks
embeddings = model.encode(chunks)


# Display information
print("Total chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)