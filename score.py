import json


def generate_report():
    with open("failures.json", "r", encoding="utf-8") as file:
        results = json.load(file)

    passed = 0
    failed = 0
    unknown = 0

    for result in results:
        status = result["status"]

        if status == "PASS":
            passed += 1
        elif status == "FAIL":
            failed += 1
        elif status == "UNKNOWN":
            unknown += 1

    total = passed + failed + unknown
    rated_total = passed + failed

    if rated_total > 0:
        score = (passed / rated_total) * 100
        score_text = f"{round(score, 1)} %"
    else:
        score_text = "Nicht berechenbar"

    report = f"""AGENT BREAKER - SECURITY REPORT
========================================

Security Score: {score_text}

Bewertete Tests: {rated_total} von {total}
PASS: {passed}
FAIL: {failed}
UNKNOWN: {unknown}

========================================
TEST RESULTS
========================================
"""

    for result in results:
        report += f"""
Kategorie: {result["category"]}
Status: {result["status"]}
Grund: {result.get("reason", "Kein Grund gespeichert.")}
Schweregrad: {result.get("severity", "Unbekannt")}
Test: {result["input"]}
Antwort: {result["response"]}
----------------------------------------
"""

    with open("security_report.txt", "w", encoding="utf-8") as file:
        file.write(report)

    print(report)
    print("Report wurde in security_report.txt gespeichert.")


if __name__ == "__main__":
    generate_report()