import re
import gradio as gr
import fitz 
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
import ollama
from PIL import Image
import io

def process_pdf(pdf_bytes, model):
    if pdf_bytes is None:
        return None, None, None
    loader = PyMuPDFLoader(pdf_bytes)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = text_splitter.split_documents(data)
    embeddings = OllamaEmbeddings(model=model)
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)
    retriever = vectorstore.as_retriever()
    return text_splitter, vectorstore, retriever

def combine_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def ollama_llm(question, context, model):
    formatted_prompt = f"Question: {question}\n\nContext: {context}"
    response = ollama.chat(model=model, messages=[{'role': 'user', 'content': formatted_prompt}])
    response_content = response['message']['content']
    final_answer = re.sub(r'<think>.*?</think>', '', response_content, flags=re.DOTALL).strip()
    return final_answer

def rag_chain(question, text_splitter, vectorstore, retriever, model):
    retrieved_docs = retriever.invoke(question)
    formatted_content = combine_docs(retrieved_docs)
    return ollama_llm(question, formatted_content, model)

def ask_question(pdf_bytes, question, model):
    text_splitter, vectorstore, retriever = process_pdf(pdf_bytes, model)
    if text_splitter is None:
        return None
    result = rag_chain(question, text_splitter, vectorstore, retriever, model)
    return {result}

custom_css = """
/* General styling */
body {
    font-family: 'Arial', sans-serif;
    background-color: #1e1e2f;
    color: #ffffff;
}

/* Title and description styling */
h1 {
    color: #ffcc00;
    font-size: 2.5em;
    margin-bottom: 0.5em;
    font-weight: bold;
}

p {
    font-size: 1.1em;
    color: #dddddd;
    margin-bottom: 1.5em;
}

/* Input and output styling */
.input, .output {
    background-color: #2a2a3b;
    border-radius: 12px;
    padding: 25px;
    margin-bottom: 25px;
    box-shadow: 0 4px 12px rgba(255, 255, 255, 0.1);
    color: #ffffff;
}

/* File upload styling */
input[type="file"] {
    border: 2px dashed #ffcc00;
    padding: 20px;
    border-radius: 12px;
    background-color: #2a2a3b;
    color: #ffcc00;
    font-size: 1em;
    text-align: center;
    cursor: pointer;
}

input[type="file"]:hover {
    background-color: #3a3a4b;
}





/* Button styling */
button {
    background-color: #ffcc00;
    color: #1e1e2f;
    border: none;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 1em;
    cursor: pointer;
    transition: background-color 0.3s ease;
    margin-top: 10px;
    font-weight: bold;
}

button:hover {
    background-color: #e6b800;
}

/* Answer box styling */
.output-text {
    font-size: 1.2em;
    color: #ffffff;
    padding: 20px;
    background-color: #2a2a3b;
    border-radius: 8px;
    margin-top: 20px;
}
"""

# Define the Gradio interface with updated UI design
interface = gr.Interface(
    fn=ask_question,
    inputs=[
        gr.File(label="Upload PDF (optional)", file_types=[".pdf"], elem_id="file-upload"),
        gr.Textbox(label="Ask a question", placeholder="Enter your question here...", lines=2, elem_id="question-box"),
        gr.Dropdown(label="Select Model", choices=["deepseek-r1:1.5b", "deepseek-r2:3b", "deepseek-r3:7b"], value="deepseek-r1:1.5b", elem_id="model-selector")
    ],
    outputs=gr.Textbox(label="Answer", placeholder="Your answer will appear here...", elem_id="answer-box"),
    title="Professional Document Query Assistant",
    description="AI-powered PDF query assistant.",
    css=custom_css,
    theme="default",
    live=False,
)

interface.launch()
