import re
from datetime import datetime, timedelta
from dateutil import parser as date_parser

def parse_tanya(question: str):
    """
    Parsing pertanyaan user menjadi:
    - tipe_laporan: jenis laporan
    - start_date: tanggal awal
    - end_date: tanggal akhir
    """

    question = question.lower()

    # Default: hari ini
    today = datetime.today().date()
    start_date = end_date = today

    # Deteksi jenis laporan
    if "pasien" in question:
        tipe_laporan = "pasien_regis"
    elif "pendapatan" in question:
        tipe_laporan = "pendapatan"
    else:
        tipe_laporan = "tidak_diketahui"

    # Deteksi periode waktu
    if "hari ini" in question:
        start_date = end_date = today
    elif "kemarin" in question:
        start_date = end_date = today - timedelta(days=1)
    elif "bulan ini" in question:
        start_date = today.replace(day=1)
        end_date = today
    elif "bulan kemarin" in question:
        first_of_this_month = today.replace(day=1)
        last_month_end = first_of_this_month - timedelta(days=1)
        start_date = last_month_end.replace(day=1)
        end_date = last_month_end
    else:
        # Tangkap tanggal manual, misal: "1/1/2024" atau "1 Jan 2024"
        date_matches = re.findall(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}', question)
        if date_matches:
            try:
                parsed_date = date_parser.parse(date_matches[0], dayfirst=True).date()
                start_date = end_date = parsed_date
            except Exception:
                pass

    return {
        "tipe_laporan": tipe_laporan,
        "tanggal1": start_date,
        "tanggal2": end_date
    }
