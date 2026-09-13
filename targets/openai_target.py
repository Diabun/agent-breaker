import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def run_target(user_input):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "Kein OpenAI API-Key gefunden. "
            "Bitte OPENAI_API_KEY in der .env eintragen."
        )

    client = OpenAI(
        api_key=api_key
    )

    try:
        response = client.responses.create(
            model="gpt-5.6-luna",
            input=user_input,
            max_output_tokens=100
        )

    except Exception as error:
        raise RuntimeError(
            f"OpenAI API-Fehler: {error}"
        )

    if not response.output_text:
        raise RuntimeError(
            "OpenAI hat keine Antwort zurückgegeben."
        )

    return response.output_text