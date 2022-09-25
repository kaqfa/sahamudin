import streamlit as st
import pandas as pd

@st.cache
def load_company():
    companies = pd.read_csv('./files/company_info-600-700.csv')
    return companies

def main():
    st.title("Tampilan Saham Biasanya")
    st.sidebar.title("Tampilan Saham")

    companies = load_company()
    sector = st.selectbox('Sektor', companies['sector'].unique())
    cities = st.multiselect('Kota Persh', companies['city'].unique())

    if sector :
        companies = companies[companies['sector'] == sector]
    if cities :
        companies = companies[companies['city'].isin(cities)]
        
    st.dataframe(data=companies[['symbol', 'website', 'city', 'sector', 'fullTimeEmployees']], use_container_width=True)

if __name__ == '__main__':
    main()