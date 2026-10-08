# AI Document Question Answering System

## Project Overview

This project is an AI-powered document question-answering system that allows users to ask questions about the contents of a PDF document.

The system uses a Retrieval-Augmented Generation (RAG) approach. It extracts text from the PDF, divides the text into smaller chunks, converts the chunks into embeddings, and uses FAISS to retrieve the most relevant information for a user's question. Gemini then generates an answer using the retrieved context.

## Technologies Used

- Python
- PyPDF2
- Sentence Transformers
- FAISS
- Google Gemini API
- python-dotenv
- streamlit

## How the System Works

1. The user uploads a PDF through the Streamlit web interface.
2. The PDF text is extracted using PyPDF2.
3. The extracted text is divided into smaller chunks.
4. Each chunk is converted into a numerical embedding using Sentence Transformers.
5. The embeddings are stored in a FAISS index.
6. The user enters a question through the Streamlit interface.
7. The question is converted into an embedding and compared with the document embeddings.
8. FAISS retrieves the most relevant chunks.
9. The retrieved chunks are provided as context to Gemini.
10. Gemini generates an answer based only on the retrieved context.
11. The answer and retrieved source chunks are displayed in the Streamlit interface.


## Streamlit Interface

The project includes a Streamlit-based web interface that makes the document question-answering system easy to use.

Users can:

- Upload their own PDF document
- Ask questions about the uploaded document
- View AI-generated answers
- View the retrieved source chunks used to generate the answer

The Streamlit interface provides the front end, while the RAG pipeline handles document processing, semantic search, and answer generation.


## Project Structure

```text
AI_yhills_project/
│
├── main.py
├── pdf_reader.py
├── embedding_test.py
├── Model Ans Odd 2024.pdf
├── requirements.txt
├── README.md
└── .env.example
