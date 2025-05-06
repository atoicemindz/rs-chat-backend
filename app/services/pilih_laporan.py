from sqlalchemy import text
from app.extensions import db

def pilih_lap(data_parsing):
    laporan = data_parsing['tipe_laporan']
    tanggal_awal = data_parsing['tanggal1']
    tanggal_akhir = data_parsing['tanggal2']

    if laporan == 'pasien_regis':
        return pasien_regis(tanggal_awal, tanggal_akhir)
    
    return {"error": "Jenis laporan tidak dikenali"}

def pasien_regis(tanggal_awal, tanggal_akhir):
    query = f" SELECT rj,ri FROM dbo.f_pasien_regis(:awal,:akhir) "
    result = db.session.execute(text(query), {'awal': tanggal_awal, 'akhir': tanggal_akhir})
    row = result.fetchone()
    if row:
        return {'rawat_jalan': row.rj, 'rawat_inap': row.ri}
    
    return {'rawat_jalan': 0, 'rawat_inap': 0}
