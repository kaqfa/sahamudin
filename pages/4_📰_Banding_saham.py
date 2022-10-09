import streamlit as st
from yfinance import Ticker
from functions.loader import load_company
import pandas as pd

def main():
    companies = load_company()
    list_saham = [f'{company.symbol} : {company.shortName}' for num, company in companies.iterrows()]
    sahams = st.multiselect('Pilih Saham (Max 3)', list_saham)
    if sahams:
        history_list = []
        for saham in sahams:
            emitens = Ticker(saham[:4]+".JK")
            data_hist = emitens.history(period='6mo', interval='1d')
            data_hist['Symbol'] = saham[:4]+".JK"
            data_hist = data_hist[['Symbol', 'Close']].reset_index()
            history_list.append(data_hist)
        histories = pd.concat(history_list, ignore_index=True)
        # st.dataframe(histories)
        st.vega_lite_chart(histories, {
            'mark': "line",
            'encoding': {
                'x': {'field': 'Date', 'type': 'temporal'},
                'y': {'field': 'Close', 'type': 'quantitative'},
                'color': {'field': 'Symbol', 'type': 'nominal'},
            },
        }, use_container_width=True)

if __name__ == '__main__':
    main()