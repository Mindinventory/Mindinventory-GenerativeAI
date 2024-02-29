# Langgraph Chatbot with DuckDuckGo Search and OpenAI GPT-3.5 Turbo

This Python script demonstrates the implementation of a chatbot using Langgraph, DuckDuckGo Search, and OpenAI GPT-3.5 Turbo. The chatbot is designed to perform internet searches and retrieve information based on user queries.

## Dependencies

- `langchain`: Langchain library for language processing.
- `langgraph`: Langgraph library for creating stateful workflows.
- `langchain_openai`: Langchain OpenAI integration for GPT-3.5 Turbo.
- `duckduckgo-search`: DuckDuckGo Search library for internet searches.
- `beautifulsoup4`: Beautiful Soup library for web scraping.

Install the required dependencies:

```bash
pip install langchain langgraph langchain_openai duckduckgo-search beautifulsoup4
```

## Langgraph Chatbot Features

### Langchain Components

1. **ChatOpenAI Model**: Uses GPT-3.5 Turbo from OpenAI for natural language understanding.

2. **Internet Search Tool (`internet_search`) and Content Processing Tool (`process_content`)**: Implements DuckDuckGo Search for internet searches and web scraping for content extraction.

### Langgraph Workflow

1. **Agent Creation**: Defines a supervisor and two worker agents - `Web_Searcher` and `Insight_Researcher`.

2. **Workflow Setup**: Creates a state graph representing the workflow with a supervisor node overseeing the workers.

3. **Agent Execution**: Utilizes Langchain to execute the chatbot workflow based on user input and agent interactions.

## Usage

1. **Install Dependencies**: Make sure to install all required dependencies mentioned above.

2. **Set Up OpenAI API Key**: Replace the placeholder `"api"` in the `ChatOpenAI` instantiation with your actual OpenAI API key.

3. **Run the Script**: Execute the provided Python script in your preferred environment.

4. **Interact with the Chatbot**: The chatbot enters a loop, allowing you to input queries. The workflow involves internet searches and content processing. The supervisor determines the next action based on the user's request.

5. **Exit**: Enter 'FINISH' when all tasks are complete to exit the loop.

## Langgraph

Langgraph is a library for creating stateful workflows and pipelines using a graph-based approach. It facilitates the design of complex workflows involving multiple agents, tools, and decision-making processes.

## Usecases

- **Educational Chatbot**: Use the chatbot to search for educational content and retrieve insights on specific topics.

- **Information Retrieval**: Incorporate Langgraph to create custom workflows for information retrieval, content processing, and decision-making.

- **Workflow Automation**: Design workflows that involve multiple steps, tools, and agents to automate specific tasks.

## Important Notes

- Ensure compliance with the terms and conditions of the services used, including OpenAI and DuckDuckGo Search.

- Handle API keys securely and avoid sharing sensitive information in public repositories.

## Readme

This script demonstrates the integration of Langgraph, DuckDuckGo Search, and OpenAI GPT-3.5 Turbo to create a chatbot capable of internet searches and content processing. Follow the steps above for installation and usage.

Feel free to customize the script for your specific use cases or extend the functionality according to your requirements. Remember to respect the usage policies of external services and libraries.

## License

This script is provided under the terms of the [MIT License](LICENSE). Review and comply with the license conditions.

Happy coding!
