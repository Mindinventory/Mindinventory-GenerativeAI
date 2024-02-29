## Fine-tune Mixtral-7B for Sentiment Analysis

This repository contains code for fine-tuning the Mixtral-7B 🧠 language model for sentiment analysis on financial news headlines. The model predicts whether a news headline expresses positive, neutral, or negative sentiment.

### Requirements

- Python 3.x 🐍
- PyTorch 🔥
- Transformers 🤖
- BitsandBytes 🧑‍💻
- tqdm 📊
- pandas 🐼
- scikit-learn 📈
- datasets 📊

### Setup

1. Clone this repository.
2. Set up your Python environment.
3. Ensure access to a CUDA-enabled GPU (recommended).

### Instructions

1. Set CUDA visible devices.
2. Disable Tokenizers parallelism.
3. Disable WandB logging (optional).
4. Run the notebook.
5. Evaluate model performance.
6. Save the trained model and tokenizer.

### Data Preparation

Data should be in CSV format with "sentiment" and "text" columns.

### Training

Fine-tune the Mixtral-7B model for sentiment analysis.

### Evaluation

Evaluate model performance using accuracy, precision, recall, F1-score, and confusion matrix.

### Results

Evaluation results are saved to a CSV file.

### Acknowledgments

- Adapted from sentiment analysis research.
- Utilizes the Mixtral-7B language model for transfer learning.

For questions, get in touch with us at [Mindinventory](https://www.mindinventory.com/). 📧
