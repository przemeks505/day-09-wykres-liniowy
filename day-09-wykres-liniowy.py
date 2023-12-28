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

st.header('Wykres linowy')

chart_data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

c = (
   alt.Chart(chart_data)
   .mark_circle()
   .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.altair_chart(c, use_container_width=True)
