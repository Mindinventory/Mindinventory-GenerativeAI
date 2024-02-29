# Mamba-SSM Chatbot README

Mamba-SSM Chatbot is a Python-based chatbot system powered by Mamba-SSM, Transformers, and Causal Conv1D. It leverages the Hugging Face model zoo for natural language processing and response generation.

## Installation

To install the required dependencies, run the following command:

```bash
!pip install torch==2.1.0 \
            transformers==4.35.0 \
            causal-conv1d==1.0.0 \
            mamba-ssm==1.0.1 -q
```

## Getting Started

### 1. Importing Libraries and Initializing Model

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from mamba_ssm.models.mixer_seq_simple import MambaLMHeadModel

device = "cuda:0" if torch.cuda.is_available() else "cpu"
model_name = "clibrain/mamba-2.8b-instruct-openhermes"
chat_template_id = "HuggingFaceH4/zephyr-7b-beta"
eos_token = ""

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.eos_token = eos_token
tokenizer.pad_token = tokenizer.eos_token
tokenizer.chat_template = AutoTokenizer.from_pretrained(chat_template_id).chat_template

model = MambaLMHeadModel.from_pretrained(
    model_name,
    device=device,
    dtype=torch.float16
)
```

### 2. Running the Chatbot

```python
messages = []

def run():
    input_ids = tokenizer.apply_chat_template(
        messages, return_tensors="pt", add_generation_prompt=True
    ).to(device)

    out = model.generate(
        input_ids=input_ids,
        max_length=2048,
        temperature=0.9,
        top_p=0.3,
        eos_token_id=tokenizer.eos_token_id
    )

    decoded = tokenizer.batch_decode(out)
    response = (decoded[0].split("\\n")[-1].replace(eos_token, ""))
    messages.append(dict(role="assistant", content=response))
    print(response)
```

### 3. Providing User Prompts and Interacting with the Chatbot

```python
prompt = "List down 10 rather strange yet true psychological facts about nature"
messages.append(dict(role="user", content=prompt))
run()

prompt = "what about life?"
messages.append(dict(role="user", content=prompt))
run()
```

## Additional Notes

- The chatbot utilizes Mamba-SSM for response generation, Transformers for tokenization, and Causal Conv1D for model inference.
- The provided example demonstrates the chatbot responding to user prompts related to psychological facts about nature and life.
- Make sure to install the specified versions of torch, transformers, causal-conv1d, and mamba-ssm for compatibility.
- The chatbot's behavior can be customized by modifying the model parameters, prompts, or other settings within the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
