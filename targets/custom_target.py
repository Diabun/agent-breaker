import json
import requests


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

    data = {
        input_field: user_input
    }

    try:
        if method.upper() == "POST":
            response = requests.post(
                api_url,
                json=data,
                timeout=30
            )
        else:
            raise RuntimeError(
                f"HTTP-Methode {method} wird noch nicht unterstützt."
            )

        response.raise_for_status()

    except requests.exceptions.ConnectionError:
        raise RuntimeError(
            "Die API konnte nicht erreicht werden."
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