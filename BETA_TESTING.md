# Agent Breaker – Beta Test

Danke, dass du Agent Breaker testest!

Agent Breaker ist ein frühes Security-Testing-Tool für AI-Agenten. Es versucht, Sicherheitsprobleme wie Prompt Injection, Data Leaks und Tool Misuse zu finden.

## 1. Installation

Repository klonen:

```bash
git clone https://github.com/Diabun/agent-breaker.git
cd agent-breaker
```

Virtuelle Umgebung erstellen und unter Windows aktivieren:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Pakete installieren:

```bash
pip install -r requirements.txt
```

## 2. Eigenen Agent verbinden

Öffne:

```text
config.json
```

Trage dort die API deines Agents ein.

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

Kopiere danach `.env.example` zu `.env` und trage dort deinen echten API-Key ein:

```text
CUSTOM_API_KEY=dein_api_key
```

Speichere deinen echten API-Key niemals direkt in `config.json` und veröffentliche deine `.env` nicht.

### Beispiel mit x-api-key

Wenn deine API stattdessen einen Header wie `x-api-key` verwendet:

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

Wenn deine API keine Authentifizierung benötigt, kannst du `auth_env`, `auth_header` und `auth_prefix` aus `config.json` entfernen.

## 3. AI-Judge

Standardmässig ist der AI-Judge deaktiviert:

```text
AI_JUDGE_ENABLED=false
```

In diesem Modus verwendet Agent Breaker nur lokale Bewertungsregeln.

Wenn der AI-Judge aktiviert wird, können Test-Prompts und Antworten des Agents zur Bewertung an OpenAI gesendet werden.

## 4. Security Scan starten

```bash
python custom_scan.py
```

Agent Breaker führt danach mehrere Security-Tests gegen deinen Agenten aus.

Die Ergebnisse werden lokal in `failures.json` gespeichert.

## 5. Security Report erstellen

Nach einem erfolgreichen Scan:

```bash
python score.py
```

Der Report wird zusätzlich gespeichert als:

```text
security_report.txt
```

## 6. Feedback

Nach dem Test interessieren uns besonders diese Fragen:

1. War die Installation verständlich?
2. Konntest du deinen Agenten einfach verbinden?
3. Hat Agent Breaker ein echtes oder interessantes Problem gefunden?
4. War der Security Report verständlich und hilfreich?
5. Was hat nicht funktioniert oder war nervig?
6. Würdest du Agent Breaker nochmals verwenden?

## Wichtig

Agent Breaker befindet sich noch in einer frühen Beta-Version.

Die Ergebnisse sind keine Garantie dafür, dass ein AI-Agent sicher ist.

Teste nur Systeme und APIs, für die du die Erlaubnis zum Testen hast.