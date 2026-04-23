"""
RAG:
    1- loading for  the file 
    2- embedding model 
    
"""
# loading main data
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate



pdfs=["hrl_1.pdf","hrl_2.pdf","hrl_3.pdf","hrl_4.pdf","hrl_5.pdf"]

all_pages=[]

for pdf in pdfs:
    
    loader=PyPDFLoader(pdf)
    
    docs=loader.load()
    
    all_pages.extend(docs)
    

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

# embedding_data=Chroma.from_documents(
    
#     chunks,
#     embedding=embedding_model,
#     persist_directory="./db"
    
# )


embedding_data=Chroma(
    
  
    embedding_function=embedding_model,
    persist_directory="./db"
    
)
llm=ChatOpenAI(
    model="gemini-3-flash-preview",
    api_key=API_KEY,
    base_url=BASE_URL
)


templete_prompt=ChatPromptTemplate.from_messages([
    ("system","""
     
     You are a helpful assistant.
     
     """),
    
    ("human","""
     
     
     
     context:
     {context}
     
     question:
     {question}
     
     
     
     
     """)]
)


def context (qs):
    retriever_data=embedding_data.as_retriever(search_kwargs={"k":15}).invoke(qs)
    
    retriever_data="\n\n".join([f"{doc.page_content}" for doc in retriever_data])


    return retriever_data


def response (user_input):
    
    message=templete_prompt.format_messages(
        context=context(user_input),
        question=user_input
    )
    
    response_llm=llm.invoke(message)
    
    return response_llm.content

