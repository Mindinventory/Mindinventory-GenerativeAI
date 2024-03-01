import os
import requests
import pickle
# import numpy as np

from fastapi import FastAPI
from pydantic import BaseModel
import mydb
import user_input
from PyPDF2 import PdfReader

import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

from langchain.document_loaders import PyPDFLoader
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableLambda
from langchain.llms import OpenAI

#from langchain.schema import HumanMessage, SystemMessage
#from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

os.environ["OPENAI_API_KEY"]= st.secrets['OPENAI_API_KEY']

app= FastAPI()

@app.get('/')
async def root():
    return {'message': 'pdf-chatbot'}

@app.post('/predict')
def compute(data: user_input.User_Input):
    inputs= data.dict()
    query= inputs['query']

    query_vocabulary = set()
    tokens = query.lower().split()
    query_vocabulary.update(tokens)

    word_to_index = {word: i for i, word in enumerate(query_vocabulary)}

    vector = np.zeros(len(vocabulary))
    for token in tokens:
      vector[word_to_index[token]] += 1
    query= vector

    prompt= ChatPromptTemplate.from_template(
    '''Your role is to act like a helpful assistant who can answer questions
        about an input query based on the given data.

        Answer the following question: {question}
        by searching in the following data: {context}'''
    )
    #llm= ChatOpenAI(streaming=True,
    #            callbacks=[StreamingStdOutCallbackHandler()])
    llm= OpenAI()
    output_parser= StrOutputParser()
    setup_and_retrieval= RunnableParallel(
        {"context": RunnableLambda(vector_store.find_similiar_vectors), "question": RunnablePassthrough()}
    )
    chain= setup_and_retrieval | prompt | llm | output_parser
    wordstream= ""
    for chunk in chain.stream(query):
        wordstream+=chunk

    st.write(wordstream)

    return {'Prediction': wordstream}
    #full_response = []
    #if wordstream:
    #        full_response.append(wordstream)
    #        result = "".join(full_response).strip()
    #        with streaming_box.container():
    #            st.markdown("---")
    #            st.markdown("#### Response:")
    #            st.markdown(result)
    #            st.markdown("---")
    #st.session_state.output_text = "".join(full_response).strip()

with st.sidebar:
    st.title('fiXit PDF Chatbot')
    st.markdown('''
                ## About
                App developed using OpenAI API, Langchain, and streamlit
                ''')

st.header("Chat with your PDF")
pdf= st.file_uploader("Upload your PDF", type= 'pdf')



if pdf is not None:
    pdf_reader= PdfReader(pdf)

    full_text= ""
    for page in pdf_reader.pages:
        full_text+= page.extract_text()

    vector_store= mydb.MydB()

    # create chunks
    text_splitter= RecursiveCharacterTextSplitter(
            chunk_size= 1000,
            chunk_overlap= 200,
            length_function= len
    )
    chunks= text_splitter.split_text(text= full_text)

    vocabulary = set()
    for chunk in chunks:
        tokens = chunk.lower().split()
        vocabulary.update(tokens)

    # Assign unique indices to words in the vocabulary
    word_to_index = {word: i for i, word in enumerate(vocabulary)}

    # Vectorize the data
    chunk_vectors = {}
    for chunk in chunks:
        tokens = chunk.lower().split()
        vector = np.zeros(len(vocabulary))
        for token in tokens:
            vector[word_to_index[token]] += 1
        chunk_vectors[chunk] = vector

    # Storing in VectorStore
    for chunk, vector in chunk_vectors.items():
        vector_store.insert_vector(chunk, vector)

    query= st.text_input("Ask questions about your PDF file:")
    if query:
        response= compute(query)

