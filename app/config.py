from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

db_svr = os.getenv("DB_SERVER")
db_nm = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = quote_plus(os.getenv("DB_PASS"))
db_drv = quote_plus(os.getenv("DB_DRIVER"))

DATABASE_URL = f"mssql+pyodbc://{db_user}:{db_pass}@{db_svr}/{db_nm}?driver={db_drv}"
