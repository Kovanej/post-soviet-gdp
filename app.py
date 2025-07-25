
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/gdp_data.csv")

st.write("Ukázka dat:")
st.dataframe(df.head())
