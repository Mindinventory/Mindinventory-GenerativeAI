## Vector Store Implementation

In this PDF chatbot application, the vector store plays a crucial role in efficiently retrieving relevant information from the PDF document during chatbot interactions. The vector store implementation involves creating vector representations for chunks of the PDF content and utilizing them for quick retrieval.

### Steps for Vector Store Implementation:

1. **PDF Text Extraction:**
   - The PyPDF2 library is used to extract text from each page of the uploaded PDF document.

2. **Text Chunking:**
   - To efficiently manage and process the large amount of text, a text splitter is employed to divide the content into manageable chunks.
   - The `RecursiveCharacterTextSplitter` is used with parameters such as `chunk_size` and `chunk_overlap` to create appropriately sized text chunks.

3. **Vocabulary Generation:**
   - A vocabulary is created by tokenizing the text chunks. The set of unique tokens across all chunks forms the vocabulary.

4. **Vectorization:**
   - Each text chunk is vectorized using a bag-of-words approach. A vector is created for each chunk, where each element represents the count of a specific word in the vocabulary within the chunk.
   - The `numpy` library is employed for efficient vector operations.

5. **Indexing and Storage:**
   - A vector store, implemented using the `MydB` class, is utilized to index and store the vector representations of the text chunks.
   - The vector store allows for quick retrieval based on vector similarity when responding to user queries.

6. **User Query Processing:**
   - When a user enters a question, the query is also vectorized using the same vocabulary and bag-of-words approach.
   - The vectorized query is then used to retrieve the most relevant chunks from the vector store based on vector similarity.

7. **Langchain Integration:**
   - The Langchain pipeline incorporates the vector store into the conversational flow, enabling the chatbot to efficiently access and provide information from the PDF document.

### Benefits of Vector Store Implementation:

- **Efficient Retrieval:** The vector store allows for efficient retrieval of relevant information from the PDF document, enabling quick responses to user queries.

- **Scalability:** By vectorizing and indexing text chunks, the implementation is scalable to large documents, providing a seamless user experience.

- **Custom Embeddings:** The vector store complements the use of custom embeddings, allowing for a tailored representation of document content.

The vector store implementation enhances the overall performance of the PDF chatbot, making it capable of handling diverse user queries and providing informative responses based on the content of the uploaded PDF.

Implement RAG:<br>
  - without using langchain.vectorstores
  - using Custom Embeddings
  - using LCEL
