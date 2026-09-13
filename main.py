from targets.openai_target import run_target
from targets.custom_target import run_custom_target
from evaluator import evaluate_response


print("=" * 50)
print("AGENT BREAKER")
print("=" * 50)

print("\nWelches Target möchtest du testen?")
print("1 = OpenAI")
print("2 = Custom API")

choice = input("\nAuswahl: ")

test_input = input("\nGib einen Test-Prompt ein: ")

category = input(
    "\nKategorie eingeben "
    "(Prompt Injection / Data Leak / Tool Misuse): "
)


if choice == "1":
    print("\nOpenAI Target wird getestet...\n")
    response = run_target(test_input)

elif choice == "2":
    print("\nCustom Target wird getestet...\n")
    response = run_custom_target(test_input)

else:
    print("\nUngültige Auswahl.")
    exit()


evaluation = evaluate_response(
    response=response,
    test_input=test_input,
    category=category
)

status = evaluation["status"]
reason = evaluation["reason"]
severity = evaluation["severity"]


print("=" * 50)
print("ERGEBNIS")
print("=" * 50)

print("Status:", status)
print("Grund:", reason)
print("Schweregrad:", severity)
print("Test:", test_input)
print("Antwort:", response)