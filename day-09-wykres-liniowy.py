#%%

"""
Polecenie st.line_chart
Polecenie st.line_chart wyświetla wykres liniowy.

Co będziemy dziś budować?
Prostą aplikację, która wyświetla wykres liniowy.

Przebieg aplikacji:

Generowanie ciągu liczb losowych za pomocą biblioteki NumPy i stworzenie z nich ramki danych biblioteki Pandas.
Stworzenie i wyświetlenie wykresu liniowego przy użyciu polecenia st.line_chart().
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import altair as alt
from vega_datasets import data

st.header('Wykres linowy')

chart_data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)


st.header('Wyświetl wykres, korzystając z biblioteki Altair')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

c = (
   alt.Chart(chart_data)
   .mark_circle()
   .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.altair_chart(c, use_container_width=True)

# Motyw Altair
st.header('Spójrzmy na przykład wykresów z motywem Streamlit i natywnym motywem Altair:')


source = data.cars()

chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)