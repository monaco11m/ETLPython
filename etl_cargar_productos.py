import pandas as pd
from sqlalchemy import create_engine, text

# Replace with your actual credentials
engine = create_engine('postgresql://postgres:123456@localhost:5432/KaggleDB')

# Load the dataset from the new path
df = pd.read_csv(r"C:\Users\usuario\Downloads\Kaggle\olist_products_dataset.csv")



# Insert data into the database
try:
    df.to_sql(
        'K_Product', engine, if_exists='replace', index=False
    )
    print("✅ Data successfully loaded into dim_product table!")
except Exception as e:
    print("❌ Failed to load data.")
    print("Error:", e)
