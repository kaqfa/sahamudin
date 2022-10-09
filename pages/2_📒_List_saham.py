import streamlit as st
import pandas as pd
import numpy as np

from functions.loader import load_company

def main():
    st.markdown("## List Saham Terbaik (LQ-45)")
    
    companies = load_company()

    st.markdown("### Jumlah Emiten Per-Sektor")
    val_counts = companies['sector'].value_counts().rename_axis('unique_values').reset_index(name="counts")
    val_counts.rename(columns={'unique_values': 'Sektor', 'counts': 'Jumlah'}, inplace=True)
    print(val_counts)
    st.bar_chart(val_counts, x='Sektor', y='Jumlah')

    sectors = companies['sector'].unique()
    sectors = np.append(sectors, '-- Semua Sektor --')
    sector = st.selectbox('Sektor', sectors)

    if sector != '-- Semua Sektor --' :
        companies = companies[companies['sector'] == sector]
        
    # columns = ['symbol', 'shortName', 'longName', 'sector', 'industry', 'fullTimeEmployees', 'city', 'website', 'phone']
    columns = ['symbol', 'shortName', 'sector']
    st.dataframe(data=companies[columns], use_container_width=True)

if __name__ == '__main__':
    main()