import json

from evaluator import evaluate_response


with open("failures.json", "r", encoding="utf-8") as file:
    results = json.load(file)


for result in results:
    response = result["response"]

    new_status = evaluate_response(response)

    result["status"] = new_status


with open("failures.json", "w", encoding="utf-8") as file:
    json.dump(results, file, ensure_ascii=False, indent=4)


print("Gespeicherte Antworten wurden neu bewertet.")