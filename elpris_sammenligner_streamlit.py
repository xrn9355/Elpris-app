import streamlit as st
import pandas as pd
import requests
from dateutil import parser

st.title("⚡ Elpris Sammenligner")

st.write("Indtast dit forbrug og sammenlign elpriser mod Norlys (inkl. rabat de første 6 måneder).")

# Upload eller indtast egne priser
uploaded_file = st.file_uploader("Upload CSV med timepriser (kolonner: time, pris)", type="csv")
fixed_price = st.number_input("Eller indtast fast pris (øre/kWh)", min_value=0.0, value=0.0)

# Forbrug
annual_usage = st.number_input("Årligt forbrug i kWh", min_value=0.0, value=2000.0)

# Norlys-rabat (100 kr/måned i 6 mdr)
norlys_discount = 100
discount_months = 6

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df['time'] = pd.to_datetime(df['time'])
    avg_price = df['pris'].mean()
else:
    avg_price = fixed_price / 100  # fra øre til kr.

# Beregning
annual_cost = avg_price * annual_usage
norlys_cost = annual_cost - (norlys_discount * discount_months)

st.subheader("Resultater")
st.write(f"📊 Gennemsnitlig pris: {avg_price:.2f} kr/kWh")
st.write(f"💡 Estimeret årlig omkostning (uden rabat): {annual_cost:.0f} kr")
st.write(f"💚 Norlys med rabat ({discount_months} mdr á {norlys_discount} kr): {norlys_cost:.0f} kr")

st.write("➡️ Besparelse med Norlys første år:", f"{annual_cost - norlys_cost:.0f} kr")
