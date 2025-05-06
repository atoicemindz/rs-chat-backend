from app.extensions import db

# Contoh model tabel
class Pasien(db.Model):
  __tablename__ = 'PASIEN'

  NOPASIEN = db.Column(db.String, primary_key=True)
  NAMAPASIEN = db.Column(db.String)
  TGLLAHIR = db.Column(db.DateTime)
