import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def main():
    host = os.getenv("MAN_DB_HOST")
    port = os.getenv("MAN_DB_PORT")
    user = os.getenv("MAN_DB_USER")
    pw   = os.getenv("MAN_DB_PASS")
    db   = os.getenv("MAN_DB_NAME")

    # Add SSL parameters for Google Cloud SQL
    url = f"mysql+pymysql://{user}:{pw}@{host}:{port}/{db}?charset=utf8mb4"
    
    # Create engine with SSL
    engine = create_engine(
        url,
        connect_args={
            'ssl': {'ssl_disabled': False}
        }
    )

    df = pd.DataFrame([
        {"visit_id": 1, "reason": "Checkup"},
        {"visit_id": 2, "reason": "Flu"},
        {"visit_id": 3, "reason": "Chest pain"}
    ])

    df.to_sql("visits", engine, if_exists="replace", index=False)

    out = pd.read_sql("SELECT * FROM visits", engine)
    print(out)

if __name__ == "__main__":
    main()