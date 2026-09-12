import json

from targets.custom_target import run_custom_target
from evaluator import evaluate_response

from attacks.prompt_injection import PROMPT_INJECTION_TESTS
from attacks.data_leak import DATA_LEAK_TESTS
from attacks.tool_misuse import TOOL_MISUSE_TESTS


api_url = input("Gib die API-URL des Targets ein: ")


test_categories = {
    "Prompt Injection": PROMPT_INJECTION_TESTS,
    "Data Leak": DATA_LEAK_TESTS,
    "Tool Misuse": TOOL_MISUSE_TESTS
}


results = []


for category, tests in test_categories.items():

    print("\nKategorie:", category)
    print("=" * 50)

    for test_input in tests:

        response = run_custom_target(
            api_url,
            test_input
        )

        status = evaluate_response(response)

        print(status, "-", test_input)
        print("Antwort:", response)
        print("-" * 50)

        results.append({
            "category": category,
            "input": test_input,
            "response": response,
            "status": status
        })


with open("failures.json", "w", encoding="utf-8") as file:
    json.dump(
        results,
        file,
        ensure_ascii=False,
        indent=4
    )


print("\nScan abgeschlossen.")
print("Ergebnisse wurden in failures.json gespeichert.")