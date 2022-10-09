import pandas as pd
import streamlit as st
from yahooquery import Ticker

from functions.loader import load_company
from functions.formater import millify, periode

txt = """ ### Perusahaan {}

- Nama Panjang: {}
- Sektor & Industri: {} || {}
- Alamat: {}
- Kota: {}
- Website: {}
"""

def main():
    st.markdown("""# Informasi Tentang Saham

Inputkan kode saham yang ingin anda cari informasinya
    """)

    # kode = st.text_input("Kode Saham", placeholder="contoh: BBCA.JK", help="Cek Data Kode Saham di List Saham")
    companies = load_company()
    list_saham = [f'{company.symbol} : {company.shortName}' for num, company in companies.iterrows()]
    saham = st.selectbox('Pilih Saham', list_saham)
    
    kode = saham[:4]+".JK"
    if kode:

        kode = kode.upper()
        saham = Ticker(kode)
        
        # load profile
        result = saham.asset_profile[kode]
        
        df_emiten = pd.read_csv('./files/data_emiten.csv')
        emiten = df_emiten[df_emiten['symbol'] == kode]
        
        # show profile
        st.markdown(txt.format(emiten.shortName.values[0], emiten.longName.values[0], 
                    result['sector'], result['industry'], result['address1'], 
                    result['city'], result['website']))

        tab1, tab2, tab3, tab4 = st.tabs(["Officers", "Laba Rugi", "Arus Kas", 'Neraca Keuangan'])
        with tab1:
            officers = pd.DataFrame(result['companyOfficers']).fillna(0).astype({'age':'int'})
            st.table(officers[['name', 'age', 'title']])

        # load income
        with tab2:
            income = saham.income_statement('a', True)
            income['Total Pengeluaran'] = income['TotalExpenses'].apply(millify)
            income['Pajak Provisi'] = income['TaxProvision'].apply(millify)
            income['Total Pendapatan'] = income['TotalRevenue'].apply(millify)
            income['Periode'] = income.apply(periode, axis=1)

            show_income = income[['Periode', 'Total Pengeluaran', 'Pajak Provisi', 'Total Pendapatan']]\
                                .set_index('Periode').copy()
            show_income = show_income.T
            
            st.markdown('### Laporan Laba Rugi (income statement)')
            st.dataframe(show_income)

            st.line_chart(income[income['periodType'] == '12M'], x='Periode', y=['Total Pengeluaran', 'Total Pendapatan', 'Pajak Provisi'])

        with tab3:
            pass

        with tab4:
            pass

if __name__ == '__main__':
    main()