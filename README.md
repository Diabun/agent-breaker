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

## OpenAI API-Key

Für Funktionen mit dem AI-Judge wird ein OpenAI API-Key benötigt.

Erstelle im Projektordner eine Datei mit dem Namen:

```text
.env

Füge dort deinen API-Key ein:

```text
OPENAI_API_KEY=dein_api_key
```

## Custom API konfigurieren

Die Einstellungen befinden sich in:

```text
config.json
```

Beispiel:

```json
{
  "api_url": "http://127.0.0.1:5000/agent",
  "method": "POST",
  "auth_env": "CUSTOM_API_KEY",
  "input_field": "input",
  "output_field": "output"
}
```

Bedeutung:

- `api_url` = Adresse der Agent-API
- `method` = HTTP-Methode
- `auth_env` = Name der Umgebungsvariable mit dem API-Key
- `input_field` = Feld für den Test-Prompt
- `output_field` = Feld mit der Antwort des Agents

Wenn deine API einen Bearer-Token benötigt, speichere den echten API-Key in der `.env`:

```text
CUSTOM_API_KEY=dein_api_key
```

Wenn deine API keine Authentifizierung benötigt, kannst du `auth_env` aus der `config.json` entfernen.