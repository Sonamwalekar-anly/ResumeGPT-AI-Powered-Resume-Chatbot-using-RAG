# ResumeGPT-AI-Powered-Resume-Chatbot-using-RAG

A smart AI-powered Resume Question Answering System that allows users to upload a resume (PDF), processes the content using Retrieval-Augmented Generation (RAG), and answers questions based only on the uploaded resume.

This project uses embeddings, vector databases, document chunking, and Large Language Models (LLMs) to provide accurate responses related to the candidate's resume.

---

# 🚀 Features

- Upload Resume (PDF)
- Extract text from resume
- Split resume into meaningful chunks
- Generate embeddings
- Store embeddings in Chroma Vector Database
- Retrieve relevant resume information
- Ask natural language questions
- AI answers only from the uploaded resume
- Fast semantic search
- Modular project architecture

---

# 🛠️ Technologies Used

- Python
- LangChain
- ChromaDB
- Sentence Transformers / Embeddings
- LLM (Groq/OpenAI/Ollama)
- PDF Loader
- Retrieval-Augmented Generation (RAG)

---

# 📂 Project Structure

```
Resume-QA-System/
│
├── app.py                     # Main application
├── config.py                  # Configuration settings
├── requirements.txt
├── README.md
│
├── data/                      # Resume PDFs
│
├── chroma_db/                 # Vector database
│
├── prompts/
│   └── prompt_template.py
│
├── src/
│   ├── pdf_loader.py          # Load PDF resumes
│   ├── chunking.py            # Split text into chunks
│   ├── embeddings.py          # Generate embeddings
│   ├── vector_store.py        # Chroma vector database
│   ├── retriever.py           # Retrieve relevant chunks
│   └── rag_chain.py           # RAG pipeline
│
├── myenv/
├── venv/
└── .gitignore
```

---

# ⚙️ Working Flow

```
Resume PDF
      │
      ▼
PDF Loader
      │
      ▼
Text Extraction
      │
      ▼
Text Chunking
      │
      ▼
Embedding Generation
      │
      ▼
Chroma Vector Database
      │
      ▼
User Question
      │
      ▼
Retriever
      │
      ▼
Relevant Resume Chunks
      │
      ▼
LLM
      │
      ▼
Final Answer
```

---

# 📌 Modules Description

## 1. pdf_loader.py

Loads the uploaded PDF resume and extracts text.

---

## 2. chunking.py

Splits extracted text into smaller chunks to improve retrieval accuracy.

---

## 3. embeddings.py

Converts text chunks into numerical vector embeddings using embedding models.

---

## 4. vector_store.py

Stores all generated embeddings inside ChromaDB for semantic search.

---

## 5. retriever.py

Finds the most relevant resume chunks based on the user's query.

---

## 6. rag_chain.py

Combines the retrieved context with the LLM to generate accurate answers.

---

## 7. app.py

Main entry point of the application.

Responsible for:

- Loading resume
- Creating vector database
- Accepting user questions
- Displaying AI-generated answers

---

# 📥 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/resume-qa-system.git
```

```bash
cd resume-qa-system
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python app.py
```

or

```bash
streamlit run app.py
```

*(Depending on how your application is built.)*

---

# 📄 How to Use

1. Start the application.
2. Upload a resume in PDF format.
3. The system extracts the resume content.
4. Text is divided into chunks.
5. Embeddings are generated.
6. Embeddings are stored in ChromaDB.
7. Ask any question related to the uploaded resume.

Example Questions:

- What are the candidate's skills?
- What projects has the candidate completed?
- What is the educational background?
- Which programming languages does the candidate know?
- What certifications does the candidate have?
- Does the candidate have internship experience?
- What is the candidate's work experience?

---

# 🧠 RAG Pipeline

```
PDF Resume
      │
      ▼
Load Document
      │
      ▼
Split Text
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
      │
      ▼
User Question
      │
      ▼
Similarity Search
      │
      ▼
Relevant Chunks
      │
      ▼
LLM
      │
      ▼
Answer
```

---

# 📚 Requirements

Typical dependencies include:

- Python 3.10+
- langchain
- chromadb
- sentence-transformers
- pypdf
- python-dotenv
- openai / groq
- numpy

Install using:

```bash
pip install -r requirements.txt
```

---

# 📈 Advantages

- Fast semantic search
- Accurate resume-based answers
- Modular architecture
- Easy to extend
- Supports multiple resumes (with modifications)
- Efficient Retrieval-Augmented Generation

---

# 🔮 Future Enhancements

- Support multiple resume uploads
- Resume ranking
- ATS score prediction
- Candidate comparison
- Resume summarization
- Skill gap analysis
- Job matching
- Interview question generation
- Chat history
- Web deployment

---

# 👨‍💻 Author

**Sonam Walekar**

Data Analyst | Python Developer | AI & Machine Learning Enthusiast

---

# 📜 License

This project is developed for educational and learning purposes.

Feel free to use and modify it for academic or personal projects.

---

# ⭐ Acknowledgements

Special thanks to the open-source community and the developers of:

- LangChain
- ChromaDB
- Python
- Sentence Transformers
- Large Language Models (LLMs)

for providing the tools that made this project possible.
