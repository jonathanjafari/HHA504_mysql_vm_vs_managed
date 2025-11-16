import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("VM_DB_HOST")
port = os.getenv("VM_DB_PORT")
user = os.getenv("VM_DB_USER")
password = os.getenv("VM_DB_PASS")
dbname = os.getenv("VM_DB_NAME")

url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}"

engine = create_engine(url)

# 1. Create table + insert data
df = pd.DataFrame({
    "visit_id": [1, 2, 3],
    "reason": ["Checkup", "Flu", "Chest pain"]
})

df.to_sql("visits", con=engine, if_exists="replace", index=False)
print("Inserted rows into VM database.")

# 2. Read back from database
df2 = pd.read_sql("SELECT * FROM visits", engine)
print("Read back rows:")
print(df2)
