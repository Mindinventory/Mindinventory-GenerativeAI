from langchain.document_loaders import WikipediaLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import pprint

API_KEY= "key"

search_term= "Grand Theft Auto VI"

docs= WikipediaLoader(query= search_term, load_max_docs= 1).load()

text_splitter= RecursiveCharacterTextSplitter(
    chunk_size= 100,
    chunk_overlap= 20,
    length_function= len,
    is_separator_regex = False
)
data= text_splitter.split_documents(docs)

embeddings= OpenAIEmbeddings(openai_api_key= API_KEY)

store= Chroma.from_documents(
    data,
    embeddings,
    ids= [f"{item.metadata['source']}-{i}" for i, item in enumerate(data)],
    collection_name= "GTA-Embeddings",
    persist_directory= 'db'
)
store.persist()

template= '''You are a bot that answers about Grand Theft Auto VI, using only the context provided.
If you don't know the answer, just state that you don't know.

{context}

Question: {question}'''

prompt= PromptTemplate(
    tempate= template,
    input_variables= ['context', 'question']
)

llm= ChatOpenAI(temperature=0, model= "gpt-2", openai_api_key= API_KEY)

qa_with_source= RetrievalQA.from_chain_type(
    llm= llm,
    chain_type= "stuff",
    retriever= store.as_retriever(),
    chain_type_kwargs= {"prompt": prompt},
    return_source_documents= True
)

pprint.pprint(
    qa_with_source("Where does GTA 6 take place?")
)
