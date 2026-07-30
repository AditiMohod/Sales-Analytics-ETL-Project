import pandas as pd
from sqlalchemy import create_engine

# Read cleaned CSV
df = pd.read_csv(r"C:\Sales_ETL_Project\cleaned_data\cleaned_sales.csv")

df.columns = (
    df.columns
      .str.strip()
      .str.replace(" ", "_")
      .str.replace("-", "_"))
      
# Database details
username = "root"
password = "root1234"
host = "localhost"
database = "sales_db"

# Connect to MySQL
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

# Load CSV into MySQL
df.to_sql(
    name="sales",
    con=engine,
    if_exists="replace",   # Creates the table if it doesn't exist
    index=False)

print(" Data loaded successfully")