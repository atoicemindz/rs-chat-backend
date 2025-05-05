from flask import Blueprint, request, jsonify
from app.services.openai_service import ask_chatgpt,ask_gemini
from app.services.model import SessionLocal, Pasien
from app.services.parser_tanya import parse_tanya
from app.services.pilih_laporan import pilih_lap

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
    
    hasil_parsing = parse_tanya(user_input)
    if not hasil_parsing:
        return jsonify({'error': 'Gagal memproses pertanyaan'}), 500
    
    hasil_laporan = pilih_lap(hasil_parsing)
    return jsonify(hasil_laporan)

    # ai_response = ask_chatgpt(user_input)
    # ai_response = ask_gemini(user_input)
    # return jsonify({"response": ai_response}), 200

@main_bp.route("/pasien", methods=["GET"])
def get_pasien():
    db = SessionLocal()
    try:
        pasien_list = db.query(Pasien).limit(10).all()
        result = [{"id": p.NOPASIEN, "nama": p.NAMAPASIEN, "tgl_lahir": p.TGLLAHIR.strftime("%Y-%m-%d")} for p in pasien_list]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        db.close()