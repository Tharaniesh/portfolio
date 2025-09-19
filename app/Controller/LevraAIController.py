# levracontroller.py
from flask import Blueprint, current_app, redirect, render_template, request, url_for
from flask import jsonify
import json
import os

levra_bp = Blueprint("levra", __name__, template_folder="../templates/levra")

class LevraAIController:
    def __init__(self):
        pass


controller = LevraAIController()

@levra_bp.route("/response", methods=["GET", "POST"])
def levraResponse():
   # Absolute path to JSON
    json_file = os.path.join(current_app.root_path, "data", "responses.json")
    with open(json_file, "r", encoding="utf-8") as f:
        responses = json.load(f)
    secret_file = os.path.join(os.path.dirname(__file__), "..", "..", "training_key.txt")
    with open(secret_file, "r") as f:
        training_key = f.read().strip()
    if request.method == "POST":
        message = request.form.get("message", "")
        if message.startswith(training_key):
            return redirect(url_for("levra.trainLevra", key=message))
    message = message.strip().lower()
    reply = responses.get(message, "Sorry, I don't have a response for that yet.")
    return jsonify({"content": reply})

@levra_bp.route("/startLevra")
def startLevra():
    return render_template("AI/LevraAI.html")

# Train mode

@levra_bp.route("/trainLevra")
def trainLevra():
    print("Training Levra...")
    key = request.args.get("key", "")
    if not key.startswith(key):
        return jsonify({"content": "Unauthorized access to training mode."})
    return jsonify({"content": f"Entering Training mode."})