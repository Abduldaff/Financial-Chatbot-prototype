# BCG Financial Chatbot Prototype

## 1. Project Overview

This project is a simplified rule-based financial chatbot prototype developed as part of the BCG GenAI simulation.

The purpose of the chatbot is to provide quick responses to predefined financial queries using financial data analyzed in Task 1.

The chatbot focuses on financial information for Microsoft, Tesla, and Apple for the years 2023–2025.

## 2. Technologies Used

* Python
* Basic conditional logic (`if`, `elif`, `else`)
* Python `input()` function

## 3. How the Chatbot Works

The chatbot receives a user's question as text and converts it to lowercase for comparison.

It then uses predefined `if-elif-else` rules to identify supported questions and return the corresponding financial response.

If the question does not match any predefined query, the chatbot returns a message explaining that it can only answer supported financial questions.

## 4. Predefined Queries

The chatbot currently supports the following queries:

1. What was Microsoft's total revenue in 2025?
2. What was Tesla's net income in 2024?
3. What was Apple's total revenue in 2025?
4. What was Microsoft's operating cash flow in 2025?
5. What was Apple's net income in 2025?

## 5. Example

### User

What was Microsoft's total revenue in 2025?

### Chatbot

Microsoft's total revenue in 2025 was $281.72 billion.

## 6. Testing

The chatbot was tested using both supported and unsupported queries.

Supported queries returned the corresponding financial information.

Unsupported queries returned a fallback response explaining the chatbot's limitations.

## 7. Limitations

The current prototype has several limitations:

* It only supports predefined questions.
* It does not understand complex natural language.
* It cannot answer questions outside the predefined financial information.
* It does not use natural language processing or machine learning.
* Financial responses are based on predefined values rather than real-time financial data.
* The chatbot does not maintain conversation history.

## 8. Future Improvements

The prototype could be extended by:

* Adding natural language processing.
* Connecting directly to financial databases.
* Supporting more companies and financial metrics.
* Adding dynamic data retrieval.
* Implementing machine learning or large language models.
* Developing a web-based user interface.
* Adding conversation history and context management.

## 9. Conclusion

This prototype demonstrates the basic principles of a rule-based financial chatbot. It provides accurate responses to a predefined set of financial queries and demonstrates how financial data can be transformed into an interactive conversational interface.

The project provides a foundation for more advanced chatbot capabilities involving NLP, machine learning, dynamic data integration, and AI-powered financial analysis.
