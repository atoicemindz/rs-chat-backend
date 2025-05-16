import re
from datetime import datetime
from app.services.ai_service import ask_ai

def parse_tanya(question: str):
    question = question.lower()
    
    today = datetime.today().date()
    start_date = end_date = today
    
    if "pasien" in question:
        tipe_laporan = "pasien_regis"
    elif "pendapatan" in question:
        tipe_laporan = "uang_kasir"
    else:
        tipe_laporan = "NA"

    start_date, end_date = detect_tanggal(question, today)
    
    return {
        "tipe_laporan": tipe_laporan,
        "tanggal1": start_date.strftime("%d/%m/%Y"),
        "tanggal2": end_date.strftime("%d/%m/%Y")
    }

def detect_tanggal(question: str, today: datetime.date):
    prompt = (
        "Dari pertanyaan berikut, ekstrak tanggal awal dan tanggal akhir yang dimaksud. "
        f"Jika tidak ada, gunakan tanggal hari ini ({today.strftime('%d/%m/%Y')}).\n\n"
        f"Contoh format output: {{\"tanggal_awal\": \"01/01/2024\", \"tanggal_akhir\": \"31/01/2024\"}}\n\n"
        f"Pertanyaan: \"{question}\""
    )
    try:
        response = ask_ai(prompt)
        match = re.search(r'"tanggal_awal"\s*:\s*"(\d{2}/\d{2}/\d{4})".*?"tanggal_akhir"\s*:\s*"(\d{2}/\d{2}/\d{4})"', response)
        if match:
            d1 = datetime.strptime(match.group(1), "%d/%m/%Y").date()
            d2 = datetime.strptime(match.group(2), "%d/%m/%Y").date()
            return d1, d2
    except Exception:
        pass
    return today, today