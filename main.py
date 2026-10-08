
from dotenv import load_dotenv
import os
from google import genai
import streamlit as st

load_dotenv(".env", override=True)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
import faiss

# Read the doc
st.title("AI Document Question Answering System")

st.write("Upload a PDF and ask questions about its content.")

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file is None:
    st.info("Please upload a PDF to continue.")
    st.stop()

reader = PdfReader(uploaded_file)

text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"


# Create chunks
chunk_size = 300
overlap=50

chunks = []

for i in range(0, len(text), chunk_size-overlap):
    chunk = text[i:i + chunk_size]
    chunks.append(chunk)


# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings for all chunks
embeddings = model.encode(chunks)

print("Total chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)

#create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)
print("FAISS index created!")
print("Number of vectors:", index.ntotal)

#semantic search- Ask a question

q=st.text_input("Ask a question:")
ask_button = st.button("Ask Question") 
if ask_button:

    if not q:
        st.warning("Please enter a question.")
        st.stop()
        
q_embedding=model.encode([q])

d,indices=index.search(q_embedding,k=2)  # find the two closest chunks

# 5. Retrieve relevant chunks

context = ""
source_chunks = []

for i in range(len(indices[0])):
    chunk_index = indices[0][i]

    context += chunks[chunk_index] + "\n\n"
    source_chunks.append(chunk_index+ 1)

# 6. Generate answer using Gemini

prompt = f"""
Answer the question only using the provided context.
If the answer is not present in the context, say that the answer was not found in the document.

Context:
{context}

Question:
{q}
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

# 7. Display final result

print("QUESTION:")
print(q)

st.subheader("AI Answer")
st.write(response.text)

st.subheader("Retrieved Sources")

for source in source_chunks:
    st.write(f"Chunk {source}")

