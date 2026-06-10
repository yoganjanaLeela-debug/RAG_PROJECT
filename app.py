from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
# -----------------------------
# Step 1: Load PDF Resumes
# -----------------------------
pdf_files = [
    "resume1.pdf",
    "resume2.pdf",
    "resume3.pdf"
]

documents = []

for pdf in pdf_files:
    loader = PyPDFLoader(pdf)
    documents.extend(loader.load())

# -----------------------------
# Step 2: Split Documents
# -----------------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

# -----------------------------
# Step 3: Create Embeddings
# -----------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# Step 4: Store in ChromaDB
# -----------------------------
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="./chroma_db"
)

print("Documents stored successfully!")

# -----------------------------
# Step 5: Load Local LLM
# -----------------------------
llm = Ollama(model="phi3")

# Other options:
# llm = Ollama(model="tinyllama")
# llm = Ollama(model="gemma:2b")
# llm = Ollama(model="mistral")

# -----------------------------
# Step 6: Query Function
# -----------------------------
def ask_question(question):

    retrieved_docs = vectorstore.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    prompt = f"""
You are a resume analysis assistant.

Use only the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response

# -----------------------------
# Step 7: Chat Loop
# -----------------------------
while True:

    query = input("\nAsk Question: ")

    if query.lower() == "exit":
        break

    answer = ask_question(query)

    print("\nAnswer:")
    print(answer)