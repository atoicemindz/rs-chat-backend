# app/services/model.py
from sqlalchemy import create_engine,Column,Integer,String,DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import DATABASE_URL

Base = declarative_base()

# Inisialisasi engine & session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Contoh model tabel
class Pasien(Base):
  __tablename__ = 'PASIEN'

  NOPASIEN = Column(String, primary_key=True, index=True)
  NAMAPASIEN = Column(String)
  TGLLAHIR = Column(DateTime)
