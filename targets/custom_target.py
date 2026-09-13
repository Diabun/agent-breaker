import json
import requests


def load_config():
    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)


def run_custom_target(user_input):
    config = load_config()

    api_url = config["api_url"]
    method = config["method"]
    input_field = config["input_field"]
    output_field = config["output_field"]

    data = {
        input_field: user_input
    }

    if method == "POST":
        response = requests.post(
            api_url,
            json=data,
            timeout=30
        )
    else:
        raise ValueError(
            f"HTTP-Methode {method} wird noch nicht unterstützt."
        )

    response.raise_for_status()

    result = response.json()

    return result[output_field]