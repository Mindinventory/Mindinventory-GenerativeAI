# PDF Document Chatbot using Llama Index and Langchain with Mistral-7B-Instruct

This Python script demonstrates the creation of a PDF document chatbot using Llama Index and Langchain, enhanced with the Mistral-7B-Instruct language model. The chatbot allows users to ask questions related to the content of the provided PDF document, and the Mistral-7B-Instruct model is utilized for natural language understanding.

## Usecase

The chatbot is designed to answer questions about the content of a specific PDF document related to the 17 Sustainable Development Goals (SDGs) adopted by the United Nations. Users can interact with the chatbot by inputting questions, and the chatbot utilizes Llama Index, Langchain, and Mistral-7B-Instruct to generate responses.

## Dependencies

- `llama-index`: Llama Index library for similarity search.
- `langchain`: Langchain library for language processing.
- `torch`: PyTorch library for deep learning.
- `transformers`: Transformers library for natural language processing tasks.
- `sentence-transformers`: Sentence Transformers library for sentence embeddings.

Install the required dependencies:

```bash
pip install llama-index langchain torch transformers sentence-transformers
```

## Additional Dependencies for Mistral-7B-Instruct

- `llama-cpp-python`: Llama CPP library for efficient language model usage.
- `the-nlper/gte-large`: Hugging Face model for language understanding.

Ensure that CMake and necessary compiler flags are available in your environment for llama-cpp-python installation.

```bash
CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir
```

## Running the Script

1. **Install Dependencies**: Make sure all dependencies, including Llama Index and Langchain, are installed.

2. **Install Additional Dependencies for Mistral-7B-Instruct**: Install the llama-cpp-python library and the Hugging Face model.

3. **Run the Script**: Execute the provided Python script in your preferred environment. The script processes the PDF document, sets up the Llama Index, and enters a loop for user interaction.

4. **Ask Questions**: Enter questions related to the content of the provided PDF document. The chatbot will generate responses based on the similarity search and language model capabilities.

5. **Exit**: Enter '-1' to exit the loop and terminate the script.

## Mistral-7B-Instruct

Mistral-7B-Instruct is a powerful language model fine-tuned for instructional and informative tasks. It is capable of understanding complex queries and generating detailed responses.

## Use Cases

- **Educational Chatbot**: Use the chatbot to provide information and answer questions related to educational materials, documents, or textbooks.

- **Document Summarization**: Utilize Mistral-7B-Instruct to generate concise summaries of document content based on user queries.

- **Information Retrieval**: Incorporate Llama Index for efficient similarity search, enhancing information retrieval capabilities.

## Important Notes

- The provided PDF document is used for demonstration purposes. Ensure that the document is accessible and replace the URL if needed.

- Handling Llama CPP library dependencies, such as CMake and compiler flags, is essential for successful installation.

- Make sure that the required GPU and CPU dependencies are satisfied for efficient execution.

## Customization

Feel free to customize the script for your specific use case. You can modify the PDF document, change the language model, or extend the functionality as needed.

## Caution

Ensure that you comply with the licensing terms and conditions of the libraries and models used in the script. Some models may have specific usage requirements.

## License

This script is provided under the terms of the [MIT License](LICENSE). Please review and adhere to the license conditions.

Feel free to modify and enhance the script according to your requirements. Happy coding!
