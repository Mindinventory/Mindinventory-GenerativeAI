# Llama-2-7b Chatbot with Gradio Interface

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

https://github.com/UjjawalKRoy/MI-GenerativeAI/assets/148340487/04fb7b11-6a11-482b-9a7f-3f6a3f9e36ad


## Overview

Llama-2-7b Chatbot with Gradio Interface is a project that utilizes the Llama-2-7b model from Hugging Face to create a conversational interface. The chatbot is designed to provide clear and concise answers to user queries and is seamlessly integrated into a Gradio Chat Interface, making it user-friendly and accessible.

## Features

- **Llama-2-7b Model:** The project leverages the power of the Llama-2-7b language model, which is known for its large-scale capabilities in understanding and generating human-like text.

- **Gradio Interface:** The chatbot is presented through a Gradio Chat Interface, allowing users to interact with the model easily. Gradio provides a simple and intuitive UI for testing and utilizing the chatbot.

## Requirements

To set up and run the Llama-2-7b Chatbot, ensure you have the following requirements installed:

- Python 3.11 (recommended)
- PyTorch
- Transformers
- Accelerate
- Gradio
- Hugging Face Hub

Install the dependencies using the following command:

```bash
pip install torch transformers accelerate -q
pip install -q --upgrade gradio
pip install --user "huggingface_hub[cli]"
pip install --user "huggingface-hub"
pip install --upgrade huggingface_hub
```

## Usage

1. **Environment Setup:** Install the required packages as mentioned in the Requirements section.

2. **Load Llama-2-7b Model:** Execute the provided script to load the Llama-2-7b model from Hugging Face.

3. **Define Chatbot with Gradio Interface:** Use the provided script to define the chatbot with a Gradio Chat Interface.

4. **Launch Interface:** Start the Gradio interface to interact with the Llama-2-7b chatbot.

## Configuration

Customize the behavior of the Llama-2-7b chatbot by adjusting parameters in the provided script. You can modify system prompts, memory limits, and other settings to suit your specific requirements.

## Structure of Llama-2-7b Prompt

The Llama-2-7b chatbot uses a specific prompt structure, including system prompts and user messages. The `format_message` function assists in formatting messages.

```python
structure_of_llama_2_prompt= '''
<s>[INST] <<SYS>>
{{ system_prompt }}
<</SYS>>

{{ user_message }} [/INST]
'''
```

## Usecases

- **Information Retrieval:** Provide clear and concise answers to user queries on a wide range of topics.

- **Conversational Interfaces:** Integrate the chatbot into applications requiring natural language understanding and generation.

- **Educational Purposes:** Use the Llama-2-7b model for educational purposes, allowing experimentation with large language models.

## Examples

Explore the provided script and example usage to understand how to integrate the Llama-2-7b chatbot into your projects effectively.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to further customize this README to include specific details about your project, its objectives, and any additional information you find relevant.



