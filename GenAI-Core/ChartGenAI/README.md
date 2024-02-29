# ChartGenAI 📊🤖

ChartGenAI is a Python application that leverages AI models to generate SQL queries for data analysis and Python code to create interactive charts using Plotly library based on user input questions and provided datasets.

## Features ✨
- Generates SQL queries to extract relevant data from a MySQL database based on user queries.
- Utilizes Plotly library to create customizable charts such as Line Chart, Bar Chart, Histogram, Scatter Plot, Bubble Plot, and Pie Chart.
- Saves generated charts as HTML files for easy sharing and integration.

## Requirements 🛠️
- Python 3.x
- MySQL database
- Google API Key (for Google Generative AI model)
- Plotly library
- Pandas library
- MySQL Connector library
- langchain_google_genai package
- few_shots package
- dotenv library

## Installation 🚀
1. Install necessary dependencies.
2. Set up Google API Key and MySQL database connection details in a `.env` file.

## Usage 🎬
1. Run the `chartgenai.py` script.
2. Input your query about the data distribution or other aspects.
3. Choose the type of chart you want to generate.
4. View the generated SQL query and Python code to create the chart.
5. Access the generated chart in the `temp` folder as `chart.html`.

## Example 🌟
```
python chartgenai.py
```