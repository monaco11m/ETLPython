from sqlalchemy import create_engine, text
import pandas as pd

# Replace with your actual credentials
engine = create_engine('postgresql://postgres:123456@localhost:5432/mini_dwh')

try:
    # Try reading something from the database
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        for row in result:
            print("✅ Connected to PostgreSQL!")
            print("PostgreSQL version:", row[0])
except Exception as e:
    print("❌ Connection failed.")
    print("Error:", e)
