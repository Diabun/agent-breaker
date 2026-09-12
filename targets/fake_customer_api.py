from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/agent", methods=["POST"])
def agent():
    data = request.get_json()

    user_input = data["input"]

    if "Passwort" in user_input or "geheim" in user_input.lower():
        answer = "Ich kann keine geheimen Informationen preisgeben."
    else:
        answer = "Der Kunden-Agent hat erhalten: " + user_input

    return jsonify({
        "output": answer
    })


if __name__ == "__main__":
    app.run(port=5000)