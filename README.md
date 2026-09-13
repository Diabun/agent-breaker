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
- verschiedene API-Authentifizierungsheader verwenden

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
```

Wenn der AI-Judge deaktiviert bleibt, verwendet Agent Breaker nur die lokalen Bewertungsregeln.

Hinweis: Wenn der AI-Judge aktiviert ist, können Test-Prompts und Antworten des getesteten Agents an OpenAI gesendet werden.

## Custom API konfigurieren

Wenn du deinen eigenen AI-Agenten testen möchtest, kannst du seine API in `config.json` eintragen.

### Beispiel mit Bearer-Token

```json
{
  "api_url": "http://127.0.0.1:5000/agent",
  "method": "POST",
  "auth_env": "CUSTOM_API_KEY",
  "auth_header": "Authorization",
  "auth_prefix": "Bearer ",
  "input_field": "input",
  "output_field": "output"
}
```

Bedeutung:

- `api_url` = Adresse der Agent-API
- `method` = HTTP-Methode
- `auth_env` = Name der Umgebungsvariable mit dem API-Key
- `auth_header` = Name des Auth-Headers
- `auth_prefix` = Text vor dem API-Key
- `input_field` = Feld für den Test-Prompt
- `output_field` = Feld mit der Antwort des Agents

Den echten API-Key speicherst du in deiner `.env`:

```text
CUSTOM_API_KEY=dein_api_key
```

Speichere den echten API-Key niemals direkt in `config.json`.

### Beispiel mit x-api-key

Manche APIs verwenden statt eines Bearer-Tokens einen eigenen Header wie `x-api-key`.

Dann kann die Konfiguration zum Beispiel so aussehen:

```json
{
  "api_url": "http://127.0.0.1:5000/agent",
  "method": "POST",
  "auth_env": "CUSTOM_API_KEY",
  "auth_header": "x-api-key",
  "auth_prefix": "",
  "input_field": "input",
  "output_field": "output"
}
```

Agent Breaker sendet den API-Key dann über den `x-api-key`-Header.

Wenn deine API keine Authentifizierung benötigt, kannst du `auth_env`, `auth_header` und `auth_prefix` aus `config.json` entfernen.

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
- Test
- Antwort des Agents

## Vollständigen Custom-API-Scan starten

Um alle vorhandenen Security-Tests gegen deine konfigurierte API auszuführen:

```bash
python custom_scan.py
```

Die Ergebnisse werden in `failures.json` gespeichert.

## Security Report erstellen

Nach einem erfolgreichen Scan:

```bash
python score.py
```

Der Report zeigt unter anderem:

- Security Score
- Anzahl PASS, FAIL und UNKNOWN
- wichtigste Sicherheitsprobleme
- unklare Ergebnisse
- alle Testergebnisse

Der Report wird zusätzlich gespeichert als:

```text
security_report.txt
```

## Beta-Test

Eine kurze Anleitung für Beta-Tester findest du in:

```text
BETA_TESTING.md
```

## Wichtig

Teste nur AI-Agenten und APIs, für die du die Erlaubnis zum Testen hast.

Agent Breaker befindet sich noch in einer frühen Entwicklungsphase. Die Ergebnisse sind keine Garantie dafür, dass ein AI-Agent vollständig sicher ist.