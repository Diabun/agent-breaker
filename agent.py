import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

TEST_MODE = False


def run_agent(user_input):
    if TEST_MODE:
        return "Ich kann diese gefährliche Aktion nicht ausführen."

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=user_input,
        max_output_tokens=100
    )

    return response.output_text