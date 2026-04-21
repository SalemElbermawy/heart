"""
RAG:
    1- loading for  the file 
    2- embedding model 
    
"""
# loading main data
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

loader=PyPDFLoader()

pdfs=[]

all_pages=[]

for pdf in pdfs:
    
    docs=loader("")
    
    pdfs.extend(docs)
    

API_KEY  = "sk-hc-v1-d8fc9e3a93924a1a9033b783cec593ad6b6f572b141f43eaa80d03f0934545f7"
BASE_URL = "https://ai.hackclub.com/proxy/v1"

embedding_model=OpenAIEmbeddings(
    model="openai/text-embedding-3-small",
    base_url=BASE_URL,
    api_key=API_KEY
)

from langchain_text_splitters import RecursiveCharacterTextSplitter
chunker=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)

chunks=chunker.split_documents(all_pages)

embedding_data=Chroma.from_documents(
    
    chunks,
    embedding=embedding_model,
    persist_directory="./db"
    
)


