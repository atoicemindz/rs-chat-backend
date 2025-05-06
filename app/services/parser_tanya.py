import re
from datetime import datetime, timedelta
from dateutil import parser as date_parser

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

def detect_tanggal(text: str, today: datetime.date):
    if "hari ini" in text:
        return today, today
    elif "kemarin" in text:
        d = today - timedelta(days=1)
        return d, d
    elif "bulan ini" in text:
        return today.replace(day=1), today
    elif "bulan kemarin" in text:
        first_of_this_month = today.replace(day=1)
        last_month_end = first_of_this_month - timedelta(days=1)
        return last_month_end.replace(day=1), last_month_end
    else:
        date_matches = re.findall(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}', text)
        if len(date_matches) >= 2:
            try:
                d1 = date_parser.parse(date_matches[0], dayfirst=True).date()
                d2 = date_parser.parse(date_matches[1], dayfirst=True).date()
                return d1, d2
            except Exception:
                pass
        elif len(date_matches) == 1:
            try:
                d = date_parser.parse(date_matches[0], dayfirst=True).date()
                return d, d
            except Exception:
                pass

    return today, today