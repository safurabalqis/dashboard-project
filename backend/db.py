# backend/db.py
import pandas as pd
from sqlalchemy import create_engine

def load_csv_to_db(csv_file='complex_sales_data.csv', db_url='sqlite:///data.db'):
    df = pd.read_csv(csv_file)
    engine = create_engine(db_url)
    df.to_sql("records", con=engine, if_exists="replace", index=False)
