
# Google Generative AI - Custom YouTube Video Assistant

The Google Generative AI library provides powerful text generation capabilities using various models. In this example, we'll explore how to use the `google.generativeai` library to create a custom YouTube video assistant using the Palm API. The assistant can generate summaries or descriptions for video content based on provided prompts.

Web-application made using Google's PaLM 2, LangChain, Streamlit, FAISS

https://github.com/UjjawalKRoy/MI-GenerativeAI/assets/148340487/d52dc9a3-faaa-437b-8f80-1013f5740061


## Installation

```bash
!pip install -q google-generativeai
```

## Setup

Make sure you have a Google API key and configure it in the script.

```python
import google.generativeai as palm

# Replace 'GOOGLE_API_KEY' with your actual API key
palm.configure(api_key="GOOGLE_API_KEY")
```

## Model Selection

List available models that support text generation.

```python
models = [n for n in palm.list_models() if "generateText" in n.supported_generation_methods]

for i in models:
    print("Model Name:", i.name)
```

Choose a model for text generation. For this example, let's use the `models/text-bison-001` model.

```python
model = models[0].name
```

## Generate Text

Define a prompt and use the selected model to generate text.

```python
prompt = """
Summarize this paragraph and detail some relevant context.
Text: "Johannes Gutenberg (1398 – 1468) was a German goldsmith and publisher who introduced printing to Europe...
...society from to the contemporary knowledge-based economy."

Summary: The German Johannes Gutenberg introduced printing in Europe. His invention had a decisive contribution in the spread of mass learning and in building the basis of the modern society.
"""

gen = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0.4,
    max_output_tokens=800
)
print(gen.result)
```

This script demonstrates how to use the Palm API to generate a summary based on the provided prompt.

## Custom YouTube Video Assistant

To use this for a YouTube video assistant, you can modify the prompt to ask for a video summary or description. For example:

```python
prompt = """
Generate a summary or description for the following YouTube video:
Video Title: "Exploring Ancient Architecture"
Video URL: "https://www.youtube.com/watch?v=example"
"""

gen = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0.4,
    max_output_tokens=800
)
print(gen.result)
```

Replace the video title and URL in the prompt with the actual details of the YouTube video you want a summary for.

This script can be integrated into a larger application or system to automatically generate descriptions or summaries for YouTube videos. Adjust the prompt and use it according to your specific requirements.
