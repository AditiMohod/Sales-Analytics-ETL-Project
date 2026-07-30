import pandas as pd

# Read dataset
df = pd.read_csv(r"C:\Sales_ETL_Project\data\superstore.csv",encoding="latin1")

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Clean column names
df.columns = df.columns.str.strip()

# Remove extra spaces from Customer Name
df["Customer Name"] = df["Customer Name"].str.strip()

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Save cleaned dataset
df.to_csv(r"C:\Sales_ETL_Project\cleaned_data\cleaned_sales.csv",index=False)

print("\nCleaning Completed Successfully")