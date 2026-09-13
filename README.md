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

## Installation

Repository herunterladen:

```bash
git clone https://github.com/Diabun/agent-breaker.git
```

In den Projektordner wechseln:

```bash
cd agent-breaker
```

Virtuelle Umgebung erstellen:

```bash
python -m venv .venv
```

Virtuelle Umgebung unter Windows aktivieren:

```bash
.venv\Scripts\activate
```

Benötigte Pakete installieren:

```bash
pip install -r requirements.txt
```

## Custom API konfigurieren

Die Einstellungen befinden sich in:

```text
config.json