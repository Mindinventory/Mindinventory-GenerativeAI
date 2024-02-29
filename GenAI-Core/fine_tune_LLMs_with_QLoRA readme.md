# LangChain - ChatBot with BitsAndBytes

## Overview
This repository contains code for creating a chatbot using LangChain libraries and the BitsAndBytes quantized GPT-NeoX language model. The chatbot leverages the LangChain framework for document loading, text splitting, embeddings, and retrieval-based question answering. Additionally, it utilizes the BitsAndBytes quantization for memory-efficient training of the GPT-NeoX model.

## Dependencies
- `transformers`
- `accelerate`
- `datasets`
- `peft`
- `bitsandbytes`

Install the dependencies using the following command:
```bash
pip install transformers accelerate datasets peft bitsandbytes -q
```

## Setting up the ChatBot

### LangChain Setup
1. Import necessary modules from LangChain.
2. Set your OpenAI API key (`API_KEY` variable).
3. Define the search term for Wikipedia (`search_term` variable).
4. Load documents using WikipediaLoader with LangChain.
5. Preprocess and split the documents using RecursiveCharacterTextSplitter.
6. Generate embeddings using OpenAIEmbeddings.
7. Create a Chroma vector store from the documents.
8. Define a prompt template for the chatbot.
9. Set up the ChatOpenAI model for generating responses.
10. Create a RetrievalQA chain using the defined components.

### BitsAndBytes Setup
1. Install the required libraries: `transformers`, `peft`, `bitsandbytes`.
2. Configure BitsAndBytes with a specific quantization setup (`bnb_config`).
3. Load the GPT-NeoX model and tokenizer with quantization config.
4. Enable gradient checkpointing and prepare the model for kbit training.
5. Print the trainable parameters and their percentage.
6. Load a dataset for fine-tuning, in this case, English quotes.
7. Tokenize the dataset and set up training arguments.
8. Create a data collator for language modeling.
9. Set up the training process using the Trainer from the `transformers` library.

## Training the Model
- Execute the code to train the model on the English quotes dataset.
- The training process uses gradient accumulation, 8-bit quantization, and paged AdamW optimizer.
- Check the training progress and output directory for the saved model.

## Fine-tuning with LoRA
1. Define LoRA (Long Range Arena) configuration (`lora_config`).
2. Load the pre-trained model and configure it with LoRA.
3. Fine-tune the model using the specified LoRA configuration.

## Inference
- Use the trained model to generate responses for questions.
- Provide a prompt with context and a question to the model.
- The chatbot retrieves relevant information from the pre-processed documents.

## Running the Code
- Run the provided code in a Python environment with the required dependencies installed.
- Ensure that your OpenAI API key is set for LangChain components.

## Acknowledgments
- This project combines LangChain and BitsAndBytes to create an advanced chatbot.
- Special thanks to the LangChain and Hugging Face communities for their contributions.

## License
This project is developed by MindInventory. www.mindinventory.com
