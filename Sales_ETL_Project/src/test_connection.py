from sqlalchemy import create_engine, text

username = "root"
password = "root1234"
host = "localhost"
database = "sales_db"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT VERSION();"))
        print(" Connected Successfully!")
        print(result.fetchone())
except Exception as e:
    print(" Connection Failed")
    print(e)