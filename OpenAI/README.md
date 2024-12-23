# PDF Chatbot using OpenAI, Langchain, FastAPI and Streamlit

This is a FastAPI-based PDF chatbot application that leverages OpenAI, Langchain, and Streamlit for processing and answering user queries related to the content of a PDF document. The chatbot utilizes OpenAI for language models, Langchain for creating processing chains, and Streamlit for creating a user-friendly interface.

## Usecase

The chatbot is designed to assist users in extracting information and answering questions from a PDF document. Users can upload a PDF file and interact with the chatbot by asking questions about the document's content.

## How to Use

1. **Upload PDF**: Select a PDF file using the file uploader.

2. **Processing**: The PDF content is processed, and text is extracted for further analysis.

3. **Vectorization**: The application uses Langchain's `OpenAIEmbeddings` for vectorizing the chunks of text obtained from the PDF.

4. **Vector Store**: The vectorized chunks are stored in a FAISS vector store (`VectorStore`). If the store already exists for the uploaded PDF, it is loaded; otherwise, a new one is created and saved for future use.

5. **Ask Questions**: Users can input questions related to the PDF content. The chatbot retrieves relevant information from the vector store and utilizes Langchain's question-answering capabilities to provide answers.

6. **Prediction Output**: The answers generated by the chatbot are displayed in the Streamlit interface.

## Dependencies

- `fastapi`: Web framework for building APIs with Python.
- `pydantic`: Data validation and parsing library.
- `requests`: HTTP library for making API requests.
- `streamlit`: Interactive web app framework for creating data applications.
- `PyPDF2`: Library for reading PDF files.
- `langchain`: Language processing library with support for vector stores, embeddings, and chains.
- `faiss`: Library for efficient similarity search and clustering of dense vectors.
- `openai`: Python client for the OpenAI GPT-3 API.

## Configuration

Ensure that you have the necessary API key configured for the OpenAI GPT-3 API. Set the API key as an environment variable:

```bash
export OPENAI_API_KEY=your_openai_api_key
```

## Running the Application

Install the required dependencies:

```bash
pip install fastapi pydantic requests streamlit PyPDF2 langchain openai faiss
```

Run the application:

```bash
streamlit run your_application_script.py
```

Access the application through your web browser.

## Note

Make sure to handle API keys and sensitive information securely, and consider implementing proper authentication and authorization mechanisms in a production environment.

Feel free to customize and extend the application to suit your specific use case or integrate additional features as needed.