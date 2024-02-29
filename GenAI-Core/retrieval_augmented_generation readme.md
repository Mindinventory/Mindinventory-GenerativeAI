# langchain: Grand Theft Auto VI Q&A Bot

## Overview

This repository contains code for building a Question and Answer (Q&A) chatbot focused on Grand Theft Auto VI. The bot is designed to answer questions about GTA VI using a language model for generation and a document retrieval system based on embeddings.

## Components

### 1. WikipediaLoader
The `WikipediaLoader` module is used to fetch relevant documents about Grand Theft Auto VI from Wikipedia.

```python
from langchain.document_loaders import WikipediaLoader

API_KEY = "your_wikipedia_api_key"
search_term = "Grand Theft Auto VI"

docs = WikipediaLoader(query=search_term, load_max_docs=1).load()
```

### 2. RecursiveCharacterTextSplitter
The `RecursiveCharacterTextSplitter` module is responsible for splitting the fetched documents into smaller chunks to enhance processing efficiency.

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20, length_function=len, is_separator_regex=False)
data = text_splitter.split_documents(docs)
```

### 3. OpenAIEmbeddings
The `OpenAIEmbeddings` module is used to generate embeddings for the text chunks.

```python
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(openai_api_key=API_KEY)
```

### 4. Chroma
The `Chroma` module creates a vector store from the generated embeddings, associating each vector with its corresponding document.

```python
from langchain.vectorstores import Chroma

store = Chroma.from_documents(data, embeddings, ids=[f"{item.metadata['source']}-{i}" for i, item in enumerate(data)],
                              collection_name="GTA-Embeddings", persist_directory='db')
store.persist()
```

### 5. PromptTemplate
The `PromptTemplate` module defines the template for generating prompts for the chatbot.

```python
from langchain.prompts import PromptTemplate

template = '''You are a bot that answers about Grand Theft Auto VI, using only the context provided.
If you don't know the answer, just state that you don't know.

{context}

Question: {question}'''

prompt = PromptTemplate(template=template, input_variables=['context', 'question'])
```

### 6. ChatOpenAI
The `ChatOpenAI` module initializes the OpenAI language model for conversation.

```python
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0, model="gpt-2", openai_api_key=API_KEY)
```

### 7. RetrievalQA
The `RetrievalQA` module sets up the question-answering system, combining the language model and document retrieval.

```python
from langchain.chains import RetrievalQA

qa_with_source = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=store.as_retriever(),
                                              chain_type_kwargs={"prompt": prompt}, return_source_documents=True)
```

### 8. Example Usage
An example of using the Q&A system is provided, demonstrating how to pose a question and receive an answer along with the relevant source document.

```python
import pprint

pprint.pprint(qa_with_source("Where does GTA 6 take place?"))
```

## How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Set up your API keys for Wikipedia and OpenAI.
3. Replace `API_KEY` in the code with your actual API keys.
4. Run the script.

Feel free to explore and modify the code to suit your needs. Happy coding!
