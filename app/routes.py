from flask import Blueprint, request, jsonify
from app.extensions import db
from app.services.model import Pasien 
from app.services.parser_tanya import parse_tanya
from app.services.pilih_laporan import pilih_lap
from app.services.ai_service import ask_ai

main_bp = Blueprint('main', __name__)

@main_bp.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"}), 200

@main_bp.route("/chat_rs", methods=["POST"])
def chat_rs():
    data = request.get_json()
    prompt = data.get("message", "")

    if not prompt:
        return jsonify({"error": "Pesan kosong"}), 400
    
    hasil_parsing = parse_tanya(prompt)
    if not hasil_parsing:
        return jsonify({'error': 'Gagal memproses pertanyaan'}), 500
    
    hasil_laporan = pilih_lap(hasil_parsing)
    
    return jsonify(hasil_laporan)

@main_bp.route("/chat_ai", methods=["POST"])
def chat_ai():
    data = request.get_json()
    tanya = data.get("message", "")
    jawab = ask_ai(tanya)
    return jsonify({"response": jawab}), 200

    # ai_response = ask_ai(user_input) 
    # return jsonify({"response": ai_response}), 200

@main_bp.route("/pasien", methods=["GET"])
def get_pasien():
    try:
        pasien_list = Pasien.query.limit(10).all()
        result = [{
            "id": p.NOPASIEN,
            "nama": p.NAMAPASIEN,
            "tgl_lahir": p.TGLLAHIR.strftime("%Y-%m-%d") if p.TGLLAHIR else None
        } for p in pasien_list]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500