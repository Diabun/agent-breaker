import json

from evaluator import evaluate_response


with open("failures.json", "r", encoding="utf-8") as file:
    results = json.load(file)


for result in results:
    response = result["response"]
    test_input = result["input"]
    category = result["category"]

    evaluation = evaluate_response(
        response=response,
        test_input=test_input,
        category=category
    )

    result["status"] = evaluation["status"]
    result["reason"] = evaluation["reason"]
    result["severity"] = evaluation["severity"]


with open("failures.json", "w", encoding="utf-8") as file:
    json.dump(
        results,
        file,
        ensure_ascii=False,
        indent=4
    )


print("Gespeicherte Antworten wurden neu bewertet.")