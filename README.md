# Agent Breaker

Agent Breaker ist ein Security-Testing-Tool für AI-Agenten.

Das Tool testet AI-Agenten auf verschiedene Sicherheitsprobleme wie:

- Prompt Injection
- Data Leaks
- Tool Misuse

Agent Breaker sendet Test-Prompts an einen Agenten und bewertet danach die Antwort.

## Funktionen

Aktuell kann Agent Breaker:

- OpenAI-Agents testen
- eigene APIs testen
- verschiedene Security-Tests ausführen
- Antworten automatisch bewerten
- PASS, FAIL oder UNKNOWN vergeben
- einen Schweregrad anzeigen
- Security Reports erstellen

## Voraussetzungen

Du brauchst:

- Python
- Git
- eine virtuelle Python-Umgebung
- die benötigten Python-Pakete

## Custom API konfigurieren

Die Einstellungen befinden sich in:

```text
config.json