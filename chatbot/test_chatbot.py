# test_chatbot.py

from chatbot import simple_chatbot


test_queries = [
    "What was Microsoft's total revenue in 2025?",
    "What was Tesla's net income in 2024?",
    "What was Apple's total revenue in 2025?",
    "What was Microsoft's operating cash flow in 2025?",
    "What was Apple's net income in 2025?",
    "What is Apple's stock price?"
]


print("======================================")
print("       Chatbot Test Results")
print("======================================\n")


for query in test_queries:

    response = simple_chatbot(query)

    print("User:", query)
    print("Bot :", response)
    print("-" * 60)