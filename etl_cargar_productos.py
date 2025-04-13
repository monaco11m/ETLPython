import pandas as pd
from sqlalchemy import create_engine, text

# Replace with your actual credentials
engine = create_engine('postgresql://postgres:123456@localhost:5432/mini_dwh')

# Load the dataset from the new path
df = pd.read_csv(r"C:\Users\usuario\Downloads\Kaggle\olist_products_dataset.csv")

# Preprocessing the data
df['product_id'] = df['product_id'].astype(str)  # Ensuring correct data type
df['product_name'] = df['product_category_name'].str.strip()  # Removing leading/trailing spaces


# Insert data into the database
try:
    df[['product_id', 'product_name']].to_sql(
        'dim_product', engine, if_exists='replace', index=False
    )
    print("✅ Data successfully loaded into dim_product table!")
except Exception as e:
    print("❌ Failed to load data.")
    print("Error:", e)
