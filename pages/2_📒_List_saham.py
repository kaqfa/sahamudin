import streamlit as st
import pandas as pd


@st.cache
def load_company():
    companies = pd.read_csv('./files/data_emiten.csv')
    return companies

def main():
    companies = load_company()
    sector = st.selectbox('Sektor', companies['sector'].unique())
    cities = st.multiselect('Kota Persh', companies['city'].unique())

    if sector :
        companies = companies[companies['sector'] == sector]
    if cities :
        companies = companies[companies['city'].isin(cities)]
        
    columns = ['symbol', 'shortName', 'longName', 'sector', 'industry', 'fullTimeEmployees', 'city', 'website', 'phone']
    st.dataframe(data=companies[columns], use_container_width=True)

if __name__ == '__main__':
    main()