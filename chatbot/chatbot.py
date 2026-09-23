import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "chat_financial_data.csv"
df = pd.read_csv(DATA_FILE)

print("Dataset loaded successfully!")
print(df.head())

def simple_chatbot(user_query):

    query = user_query.lower().strip()

    if "microsoft" in query and "revenue" in query and "2025" in query:

        data = df[
            (df["Company"] == "Microsoft") &
            (df["Year"] == 2025)
        ]

        value = data["Total Revenue in USD"].iloc[0]

        return f"Microsoft's total revenue in 2025 was ${value / 1e9:.2f} billion."

    elif "tesla" in query and "net income" in query and "2024" in query:

        data = df[
            (df["Company"] == "Tesla") &
            (df["Year"] == 2024)
        ]

        value = data["Net Income in USD"].iloc[0]

        return f"Tesla's net income in 2024 was ${value / 1e9:.2f} billion."

    elif "apple" in query and "revenue" in query and "2025" in query:

        data = df[
            (df["Company"] == "Apple") &
            (df["Year"] == 2025)
        ]

        value = data["Total Revenue in USD"].iloc[0]

        return f"Apple's total revenue in 2025 was ${value / 1e9:.2f} billion."

    elif "microsoft" in query and "assets" in query and "2025" in query:

        data = df[
            (df["Company"] == "Microsoft") &
            (df["Year"] == 2025)
        ]

        value = data["Total Assets in USD"].iloc[0]

        return f"Microsoft's total assets in 2025 were ${value / 1e9:.2f} billion."

    elif "apple" in query and "liabilities" in query and "2025" in query:

        data = df[
            (df["Company"] == "Apple") &
            (df["Year"] == 2025)
        ]

        value = data["Total Liablilities in USD"].iloc[0]

        return f"Apple's total liabilities in 2025 were ${value / 1e9:.2f} billion."

    elif "tesla" in query and "cash flow" in query and "2025" in query:

        data = df[
            (df["Company"] == "Tesla") &
            (df["Year"] == 2025)
        ]

        value = data[
            "Cash Flow from operating activities in USD"
        ].iloc[0]

        return f"Tesla's operating cash flow in 2025 was ${value / 1e9:.2f} billion."

    elif "apple" in query and "net income" in query and "2025" in query:

        data = df[
            (df["Company"] == "Apple") &
            (df["Year"] == 2025)
        ]

        value = data["Net Income in USD"].iloc[0]

        return f"Apple's net income in 2025 was ${value / 1e9:.2f} billion."

    elif "tesla" in query and "assets" in query and "2024" in query:

        data = df[
            (df["Company"] == "Tesla") &
            (df["Year"] == 2024)
        ]

        value = data["Total Assets in USD"].iloc[0]

        return f"Tesla's total assets in 2024 were ${value / 1e9:.2f} billion."

    elif "microsoft" in query and "liabilities" in query and "2024" in query:

        data = df[
            (df["Company"] == "Microsoft") &
            (df["Year"] == 2024)
        ]

        value = data["Total Liablilities in USD"].iloc[0]

        return f"Microsoft's total liabilities in 2024 were ${value / 1e9:.2f} billion."

    elif "apple" in query and "cash flow" in query and "2024" in query:

        data = df[
            (df["Company"] == "Apple") &
            (df["Year"] == 2024)
        ]

        value = data[
            "Cash Flow from operating activities in USD"
        ].iloc[0]

        return f"Apple's operating cash flow in 2024 was ${value / 1e9:.2f} billion."

    elif "microsoft" in query and "net income" in query and "2023" in query:

        data = df[
            (df["Company"] == "Microsoft") &
            (df["Year"] == 2023)
        ]

        value = data["Net Income in USD"].iloc[0]

        return f"Microsoft's net income in 2023 was ${value / 1e9:.2f} billion."

    elif "tesla" in query and "revenue" in query and "2023" in query:
        data = df[
            (df["Company"] == "Tesla") &
            (df["Year"] == 2023)
        ]

        value = data["Total Revenue in USD"].iloc[0]
        return f"Tesla's total revenue in 2023 was ${value / 1e9:.2f} billion."
    else:
        return (
            "Sorry, I can only provide information about predefined "
            "financial queries for Microsoft, Tesla, and Apple."
        )

if __name__ == "__main__":

    print("======================================")
    print("   BCG Financial Chatbot Prototype")
    print("======================================")
    print("Type 'exit' to stop the chatbot.\n")

    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            print("Chatbot: Thank you for using the financial chatbot.")
            break
        response = simple_chatbot(user_query)
        print("Chatbot:", response)