from sqlalchemy import text
from app.extensions import db
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')

def pilih_lap(data_parsing):
    laporan = data_parsing['tipe_laporan']
    tgl1 = data_parsing['tanggal1']
    tgl2 = data_parsing['tanggal2']

    if laporan == 'pasien_regis':
        return pasien_regis(tgl1, tgl2)
    else:
        return {"error": "Jenis laporan tidak dikenali"}

def pasien_regis(tgl1, tgl2):
    query = f"SELECT rj, ri, tgl1, tgl2 FROM dbo.f_pasien_regis(:awal, :akhir)"
    params = {'awal': to_sql_date(tgl1),'akhir': to_sql_date(tgl2)}
    result = db.session.execute(text(query), params)
    row = result.fetchone()
    if row:
        rj = "{:,}".format(row.rj).replace(",", ".")
        ri = "{:,}".format(row.ri).replace(",", ".")
        return {"response": (
                f"Jumlah pasien yang terdaftar dari {row.tgl1} hingga {row.tgl2} adalah "
                f"{rj} untuk rawat jalan dan {ri} untuk rawat inap.")}
    return {"response": f"Tidak ditemukan data pasien dari {tgl1} hingga {tgl2}."}

def to_sql_date(tanggal_str):
    return datetime.strptime(tanggal_str, "%d/%m/%Y").strftime("%Y-%m-%d")