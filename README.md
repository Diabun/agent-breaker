# Agent Breaker

Agent Breaker ist ein Security-Testing-Tool für AI-Agenten.

Das Tool testet AI-Agenten auf verschiedene Sicherheitsprobleme wie:

- Prompt Injection
- Data Leaks
- Tool Misuse

Agent Breaker sendet Test-Prompts an einen Agenten, bewertet die Antworten und erstellt danach einen Security Report.

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
```

Füge dort deinen API-Key ein:

```text
OPENAI_API_KEY=dein_api_key
```

Teile deinen API-Key niemals öffentlich und speichere ihn nicht auf GitHub.

Ohne OpenAI API-Key kann Agent Breaker weiterhin lokale Bewertungen durchführen. Der AI-Judge wird dann nicht verwendet.

## AI-Judge aktivieren

Standardmässig ist der AI-Judge deaktiviert.

Dadurch werden unklare Agent-Antworten nicht automatisch an OpenAI gesendet.

Wenn du den AI-Judge verwenden möchtest, füge in deiner `.env` hinzu:

```text
AI_JUDGE_ENABLED=true

## Custom API konfigurieren

Wenn du deinen eigenen AI-Agenten testen möchtest, kannst du seine API in `config.json` eintragen.

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

## Einzelnen Test starten

Starte Agent Breaker mit:

```bash
python main.py
```

Danach kannst du auswählen:

```text
1 = OpenAI
2 = Custom API
```

Anschliessend gibst du einen Test-Prompt ein und wählst eine Kategorie:

```text
1 = Prompt Injection
2 = Data Leak
3 = Tool Misuse
```

Agent Breaker zeigt danach:

- Status
- Grund
- Schweregrad
- Antwort des Agents

## Vollständigen Custom-API-Scan starten

Um alle vorhandenen Security-Tests gegen deine konfigurierte API auszuführen:

```bash
python custom_scan.py
```

Die Ergebnisse werden in `failures.json` gespeichert.

## Security Report erstellen

Nach einem vollständigen Scan kannst du den Security Report erstellen:

```bash
python score.py
```

Der Report zeigt unter anderem:

- Security Score
- Anzahl PASS, FAIL und UNKNOWN
- wichtigste Sicherheitsprobleme
- unklare Ergebnisse
- alle Testergebnisse

Der Report wird zusätzlich in folgender Datei gespeichert:

```text
security_report.txt
```

## Hinweis

Teste nur AI-Agenten und APIs, für die du eine Erlaubnis zum Testen hast.

Agent Breaker befindet sich noch in Entwicklung. Die Ergebnisse sollten deshalb nicht als Garantie dafür angesehen werden, dass ein AI-Agent vollständig sicher ist.