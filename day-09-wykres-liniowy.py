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

st.header('Wykres linowy')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
