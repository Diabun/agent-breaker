import requests


def run_custom_target(api_url, user_input):
    data = {
        "input": user_input
    }

    response = requests.post(
        api_url,
        json=data,
        timeout=30
    )

    response.raise_for_status()

    result = response.json()

    return result["output"]