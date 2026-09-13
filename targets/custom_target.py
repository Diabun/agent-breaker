import json
import os

import requests
from dotenv import load_dotenv


load_dotenv()


def load_config():
    try:
        with open("config.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        raise RuntimeError(
            "config.json wurde nicht gefunden."
        )

    except json.JSONDecodeError:
        raise RuntimeError(
            "config.json enthält ungültiges JSON."
        )


def run_custom_target(user_input):
    config = load_config()

    api_url = config.get("api_url")
    method = config.get("method")
    auth_env = config.get("auth_env")
    auth_header = config.get("auth_header", "Authorization")
    auth_prefix = config.get("auth_prefix", "Bearer ")
    input_field = config.get("input_field")
    output_field = config.get("output_field")

    if not api_url:
        raise RuntimeError(
            'In config.json fehlt "api_url".'
        )

    if not method:
        raise RuntimeError(
            'In config.json fehlt "method".'
        )

    if not input_field:
        raise RuntimeError(
            'In config.json fehlt "input_field".'
        )

    if not output_field:
        raise RuntimeError(
            'In config.json fehlt "output_field".'
        )

    headers = {}

    if auth_env:
        api_key = os.getenv(auth_env)

        if not api_key:
            raise RuntimeError(
                f'Der API-Key "{auth_env}" wurde nicht in der .env gefunden.'
            )

        placeholder_values = [
            "dein_custom_api_key",
            "dein_api_key",
            "your_api_key"
        ]

        if api_key.lower() in placeholder_values:
            raise RuntimeError(
                f'Der API-Key "{auth_env}" enthält noch einen Platzhalter. '
                "Trage in der .env einen echten API-Key ein."
            )

        headers[auth_header] = f"{auth_prefix}{api_key}"

    data = {
        input_field: user_input
    }

    try:
        if method.upper() == "POST":
            response = requests.post(
                api_url,
                json=data,
                headers=headers,
                timeout=30
            )
        else:
            raise RuntimeError(
                f"HTTP-Methode {method} wird noch nicht unterstützt."
            )

        response.raise_for_status()

    except requests.exceptions.ConnectionError:
        raise RuntimeError(
            "Die API konnte nicht erreicht werden. "
            "Prüfe, ob die API-Adresse stimmt und ob die API läuft."
        )

    except requests.exceptions.Timeout:
        raise RuntimeError(
            "Die API hat zu lange für eine Antwort gebraucht."
        )

    except requests.exceptions.HTTPError:
        raise RuntimeError(
            f"Die API hat einen Fehler zurückgegeben: "
            f"HTTP {response.status_code}"
        )

    try:
        result = response.json()

    except ValueError:
        raise RuntimeError(
            "Die API-Antwort ist kein gültiges JSON."
        )

    if output_field not in result:
        raise RuntimeError(
            f'Das Feld "{output_field}" wurde '
            "in der API-Antwort nicht gefunden."
        )

    return result[output_field]