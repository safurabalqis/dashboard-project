# backend/main.py
from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd

app = FastAPI()
engine = create_engine("sqlite:///data.db")

@app.get("/data")
def get_data():
    df = pd.read_sql("SELECT * FROM records", engine)
    return df.to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
