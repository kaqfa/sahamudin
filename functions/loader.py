import streamlit as st
import pandas as pd

@st.cache
def load_company():
    companies = pd.read_csv('./files/lq45/data_emiten.csv', delimiter=";")
    return companies