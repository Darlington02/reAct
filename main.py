import os
from dotenv import load_dotenv
from langchain.agents import tool

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

@tool
def get_text_length(text: str) -> int:
    """Returns the length of a text by characters"""
    return len(text)

if __name__ == "__main__":
    print("Hello Langchain")
    print(get_text_length(text="hello langchain"))
