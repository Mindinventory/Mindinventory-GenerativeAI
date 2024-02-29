import mysql.connector
from langchain_google_genai import GoogleGenerativeAI
from langchain.utilities.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
import plotly.express as px 
import plotly.graph_objects as go
import pandas as pd
from few_shots import few_shots
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX
import os
from dotenv import load_dotenv, find_dotenv
from decimal import Decimal

load_dotenv(find_dotenv())

api_key = os.getenv('API_KEY')

llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key, max_output_tokens=5000, temperature=0.1)

db_url = os.getenv('DB_URL')

db = SQLDatabase.from_uri(db_url)

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

to_vectorize = [" ".join(example.values()) for example in few_shots]

vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=few_shots)

example_selector = SemanticSimilarityExampleSelector(
    vectorstore=vectorstore,
    k=1,
)

mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
If the user specifies in the question a specific number of examples to obtain, query for results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table. 
Assess the data in each column and try to do keyword matching using the LIKE keyword as per MySQL to get all the relevant information.
If the input question has multiple conditions, first try to give an answer which fulfills all the conditions. If this cannot be accomplished, try to give multiple outputs where each output fulfills a certain condition.
Try to select atleast 2 columns based on the input question.

Use the following format:

Question: Question here
SQLQuery: Query to run with no pre-amble
SQLResult: Result of the SQLQuery
Answer: Final answer here

No pre-amble.
"""

example_prompt = PromptTemplate(
    input_variables=["Question", "SQLQuery", "SQLResult","Answer",],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
)

few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=mysql_prompt,
    suffix=PROMPT_SUFFIX,
    input_variables=["input", "table_info"], # These variables are used in the prefix and suffix.
)

chain = SQLDatabaseChain.from_llm(llm, db, verbose=False, prompt=few_shot_prompt, return_sql=True)

query = "Give me the distribution of products across different categories."

qns = chain.invoke({"query": query})

sql_query = qns['result']
print(f'sql_query = {sql_query}')

def prep_data(sql_query):
    mysql_connection = mysql.connector.connect(host=HOST, user=YOUR_USERNAME, password=YOUR_PASSWORD, database=DB)
    cur = mysql_connection.cursor()
    try:
        cur.execute(sql_query)
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        return rows, columns
    except Exception as error:
        print(error)
    finally:
        cur.close()
        mysql_connection.close()

data = prep_data(sql_query)
# print(data)
index = [i for i in range(0, len(data[0]))]
df = pd.DataFrame(data=data[0], columns=data[1], index=index)

chart_type = input("Which type of chart would you like to create?\nAvailable options: Line Chart, Bar Chart, Histogram, Scatter Plot, Bubble Plot, Pie Chart\n")

directory = 'temp'
if not os.path.exists(directory):
    os.mkdir(directory)

prompt_template = PromptTemplate.from_template("""
You are a proficient Python developer with expertise in the Plotly library. Your objective is to generate Python code to create a {chart_type} specified by the user using the provided dataframe. 

### QUERY: 
{query}

### DATA:
{df}
                                               
### INSTRUCTIONS:
1. Begin by importing the necessary libraries (Pandas, Plotly and Decimal if needed).
2. Assess the chart type required carefully, then employ the appropriate method call exclusively for that chart type only.
3. Generate the chart specified by the user using the provided dataframe and the Plotly library.
4. Strictly AVOID specifying the 'color' parameter in the chart type method call.
5. Instead of the 'color' parameter, use SOLELY the 'color_discrete_sequence' parameter in the chart type method call to ensure the plot appears red (HEX code: #ED184F).
6. Accurately interpret and incorporate the x-axis title, y-axis title, and chart title as per the user's query and the dataset.
7. Utilize the 'update_layout' method to include the x-axis title, y-axis title, chart title, plot background color, and paper background color, setting them to blue (HEX code: #0e243b).
8. Set the font color to white (HEX code: #f7f9fa) using the 'update_layout' method.
9. Save the plot in 'chart.html' file in 'temp' folder in html format. Execute the created function with the argument as the provided dataframe, at the outer indent at the end. 
                                               
### CODE CRITERIA
- Optimize the code for efficiency and clarity.
- Avoid using incorrect syntax.
- Ensure that the code is well-commented for readability and syntactically correct.
""")

prompt = prompt_template.format(query=query, df=df, chart_type=chart_type)
result = llm.invoke(prompt).replace("```", "").replace("python", "")

print(f'code = {result}')
exec(result)
