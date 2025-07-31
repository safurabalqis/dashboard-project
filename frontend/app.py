# frontend/app.py
import streamlit as st
import pandas as pd
import requests

st.title("📊 Full System Dashboard")

response = requests.get("http://localhost:8000/data")
data = response.json()

df = pd.DataFrame(data)

st.dataframe(df)

st.bar_chart(df.select_dtypes(include=["number"]))
