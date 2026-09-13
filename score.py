import json
from datetime import datetime


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

    # Sicherheitsprobleme sammeln
    security_problems = []

    for result in results:
        if result["status"] == "FAIL":
            security_problems.append(result)

    report = f"""AGENT BREAKER - SECURITY REPORT
========================================

Erstellt am: {datetime.now().strftime("%d.%m.%Y %H:%M")}

SECURITY SCORE
========================================

Security Score: {score_text}

Gesamte Tests: {total}
Bewertete Tests: {rated_total}
PASS: {passed}
FAIL: {failed}
UNKNOWN: {unknown}

"""

    # Wichtigste Probleme
    report += """========================================
WICHTIGSTE SICHERHEITSPROBLEME
========================================
"""

    if not security_problems:
        report += "\nKeine eindeutigen Sicherheitsprobleme gefunden.\n"

    else:
        for number, result in enumerate(security_problems, start=1):
            report += f"""
Problem {number}
Kategorie: {result["category"]}
Schweregrad: {result.get("severity", "Unbekannt")}
Grund: {result.get("reason", "Kein Grund gespeichert.")}
Test: {result["input"]}
----------------------------------------
"""

    # Unklare Ergebnisse
    unknown_results = [
        result for result in results
        if result["status"] == "UNKNOWN"
    ]

    report += """
========================================
UNKLARE ERGEBNISSE
========================================
"""

    if not unknown_results:
        report += "\nKeine unklaren Ergebnisse.\n"

    else:
        for result in unknown_results:
            report += f"""
Kategorie: {result["category"]}
Grund: {result.get("reason", "Kein Grund gespeichert.")}
Test: {result["input"]}
Antwort: {result["response"]}
----------------------------------------
"""

    # Alle Tests
    report += """
========================================
ALLE TESTERGEBNISSE
========================================
"""

    for result in results:
        report += f"""
Kategorie: {result["category"]}
Status: {result["status"]}
Schweregrad: {result.get("severity", "Unbekannt")}
Grund: {result.get("reason", "Kein Grund gespeichert.")}
Test: {result["input"]}
Antwort: {result["response"]}
----------------------------------------
"""

    with open("security_report.txt", "w", encoding="utf-8") as file:
        file.write(report)

    print(report)
    print("\nReport wurde in security_report.txt gespeichert.")


if __name__ == "__main__":
    generate_report()