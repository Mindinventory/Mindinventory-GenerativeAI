# Fine-tune gemma-7B for sentiment

## Introduction
🚀 This repository contains code for fine-tuning the gemma-7B model for sentiment analysis tasks. The gemma-7B model is a language model pretrained on a large corpus of text data and can be fine-tuned for various downstream tasks, including sentiment analysis.

## Setup
🔧 Ensure that you have the necessary dependencies installed. You can set up the environment by following these steps:

1. Set the CUDA visible devices and disable tokenizers parallelism:

```python
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

## Data Preparation
📊 The dataset used for fine-tuning the model should be in CSV format with two columns: "sentiment" and "text". You can prepare the dataset by loading it using Pandas and splitting it into training, testing, and evaluation sets.

## Training
📝 To train the model, you can use the provided `train.py` script. Make sure to set the appropriate parameters such as the model name, training epochs, batch size, etc., according to your requirements.

```bash
python train.py
```

## Evaluation
🔍 After training the model, you can evaluate its performance using the `evaluate.py` script. This script will generate accuracy metrics, a classification report, and a confusion matrix to assess the model's performance on the test data.

```bash
python evaluate.py
```

## Results
📊 The trained model will be saved along with its tokenizer in the specified output directory. You can use this saved model for inference on new data or deploy it in your application.

## Conclusion
🎉 Fine-tuning the gemma-7B model for sentiment analysis can yield promising results, especially when tailored to specific domains or datasets. Experiment with different hyperparameters and architectures to optimize performance for your task.
