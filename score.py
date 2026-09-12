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

    if total > 0:
        score = (passed / total) * 100
    else:
        score = 0

    report = f"""AGENT BREAKER - SECURITY REPORT
========================================

Security Score: {round(score, 1)} %

PASS: {passed}
FAIL: {failed}
UNKNOWN: {unknown}
TOTAL: {total}

========================================
TEST RESULTS
========================================
"""

    for result in results:
        report += f"""
Kategorie: {result["category"]}
Status: {result["status"]}
Test: {result["input"]}
Antwort: {result["response"]}
----------------------------------------
"""

    with open("security_report.txt", "w", encoding="utf-8") as file:
        file.write(report)

    print(report)
    print("Report wurde in security_report.txt gespeichert.")