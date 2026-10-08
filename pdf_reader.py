from PyPDF2 import PdfReader

reader=PdfReader("Model Ans Odd 2024.pdf")

text=""
for page in reader.pages:
    text+=page.extract_text()

print(text)

#Breaking doc into smaller chunks

chunk_size=300
chunks=[]
for i in range(0,len(text),chunk_size):
    chunk=text[i:i+chunk_size]
    chunks.append(chunk)

c=1
for chunk in chunks:
    print("CHUNK",c)
    print(chunk)
    print("-------------------------------")
    c+=1