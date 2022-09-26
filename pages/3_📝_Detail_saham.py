import pandas as pd
import streamlit as st
from yahooquery import Ticker

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

    kode = st.text_input("Kode Saham", placeholder="contoh: BBCA.JK", help="Cek Data Kode Saham di List Saham")

    if kode:
        saham = Ticker(kode)
        df_emiten = pd.read_csv('./files/data_emiten.csv')
        emiten = df_emiten[df_emiten['symbol'] == kode]
        result = saham.asset_profile[kode.upper()]
        st.markdown(txt.format(emiten.shortName.values[0], emiten.longName.values[0], 
                    result['sector'], result['industry'], result['address1'], 
                    result['city'], result['website']))

        officers = pd.DataFrame(result['companyOfficers']).fillna(0).astype({'age':'int'})
        st.table(officers[['name', 'age', 'title']])

if __name__ == '__main__':
    main()