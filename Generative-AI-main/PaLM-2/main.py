from dotenv import load_dotenv
import streamlit as st
import textwrap
from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm

from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import LLMChain
from langchain.document_loaders import YoutubeLoader
from langchain.vectorstores import FAISS
load_dotenv()

embeddings= GooglePalmEmbeddings()

def create_vector_db_from_yt_url(url: str)->FAISS:
    loader= YoutubeLoader.from_youtube_url(url)
    transcript= loader.load()
    text_splitter= RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap= 100)

    docs= text_splitter.split_documents(transcript)
    database= FAISS.from_documents(docs, embeddings)
    return database

def get_response_from_query(database, query, k= 4):
    docs= database.similarity_search(query, k= k)
    docs_page_content= "".join([d.page_content for d in docs])

    llm= GooglePalm(temperature= 0.7)
    prompt= PromptTemplate(
        input_variables= ["question", "docs"],
        template="""
        Your role is to act like a helpful Youtube assistance who can answer questions
        about on an input video based on its transcript.

        Answer the following question: {question}
        by searching the following video transcript: {docs}

        Only use the information from the transcript to answer the questions.

        If you fell like you don't have sufficient information to answer the question,
        say "I don't know"

        Your answers should be detailed.
        """
    )
    chain= LLMChain(llm= llm, prompt= prompt)
    response= chain.run(question= query, docs= docs_page_content)
    response= response.replace("\n", " ")
    return response, docs

st.title("Custom Youtube Video Assistant")
with st.sidebar:
    with st.form(key= "mu_form"):
        youtube_url= st.sidebar.text_area(
            label= "Hi!, Let's get started. What is the YouTube video's URL?",
            max_chars= 50
        )
        query= st.sidebar.text_area(
            label= "Ask me your doubts about this video.",
            max_chars= 100,
            key= "query"
        )
        submit_button= st.form_submit_button(label= "Submit")

if  query and youtube_url:
    db= create_vector_db_from_yt_url(youtube_url)
    response, docs= get_response_from_query(db, query)
    st.subheader("Answer:")
    st.text(textwrap.fill(response, width= 80))
