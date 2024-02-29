# Llama Index for Document Search and Re-Ranking

## Introduction
🔍 This repository contains code for setting up and using the Llama Index, an advanced document search tool that leverages state-of-the-art language models and embeddings for efficient information retrieval.

## Installation
To get started, install the required dependencies by running the following command:

```bash
!pip install -q pypdf llama-index einops accelerate sentence-transformers
```

Additionally, you may need to install the `llama-cpp-python` package:

```bash
!CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir
```

## Usage
1. **Load Documents:** 
   Load documents from a directory using the `SimpleDirectoryReader` class.

2. **Initialize Llama Index:** 
   Initialize the Llama Index with your preferred language model and parameters.

3. **Build Index:** 
   Build the vector store index from the loaded documents.

4. **Query Engine:** 
   Set up the query engine for conducting document search.

5. **Perform Search:** 
   Input queries to retrieve relevant documents efficiently.

## Conclusion
🚀 With the Llama Index, you can streamline your document search process and access relevant information quickly and effectively.
