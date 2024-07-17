import altair as alt
import pandas as pd
import plotly.express as px
import streamlit as st
import pression_index_st as sn


larga = pd.read_csv("static/larga_player.csv")
data = pd.read_csv("static/played_minutes.csv")
# ----------------- game start --------
radar_player = "J. Musiala"

fig = sn.make_bar_plot_player(larga, radar_player)

PAGE_TITLE = "Indices de presión | NIES"
PAGE_ICON = "🇮🇹"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.subheader("La relación entre los índices de presión")
"""
Si sumamos todo el momento generado por cada equipo, la inclinación del momento es la proporción del
momento de cada equipo.
Por ejemplo, el último partido de la Serie A 2023-24 fue entre Atalanta vs Fiorentina.
La inclinación del momento fue 65.5% para el Atalanta y 34.5% para la Fiorentina.
Para cada equipo tenemos 38 valores de inclinación del momento, un por cada partido que jugaron.
Por ejemplo, para Atalanta 22.4% y 94.7% son sus inclinaciones menores y mayores durante el torneo.

La descripción completa la encontrarás en la entrada [La inclinación del momento y la calidad de un equipo](https://www.nies.futbol/2024/06/la-inclinacion-del-momento-y-la-calidad.html).
"""
st.plotly_chart(fig)


st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
