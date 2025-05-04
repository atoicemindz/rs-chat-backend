from flask import Blueprint, request, jsonify
from app.services.openai_service import ask_chatgpt,ask_gemini

main_bp = Blueprint('main', __name__)

@main_bp.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"}), 200

@main_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "Pesan kosong"}), 400

    # ai_response = ask_chatgpt(user_input)
    ai_response = ask_gemini(user_input)
    return jsonify({"response": ai_response}), 200
