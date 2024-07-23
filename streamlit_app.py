import json
import streamlit as st
import pandas as pd
import altair as alt


pressure = pd.read_csv("static/quality_and_pression_index.csv")
# ----------------- game start --------

PAGE_TITLE = "Indices de presión | NIES"
PAGE_ICON = "🇮🇹"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.subheader("La relación entre los índices de presión")
"""
La inclinación del momento describe el porcentaje de todo el momento generado que pertenece a un
equipo. Es decir, si sumamos todo el momento generado en un partido, la inclinación del momento es
la proporción del momento de cada equipo.
Por ejemplo, el último partido de la Serie A 2023-24 fue entre Atalanta vs Fiorentina.
La inclinación del momento fue 65.5% para el Atalanta y 34.5% para la Fiorentina.
Para cada equipo tenemos 38 valores de inclinación del momento, un por cada partido que jugaron.
Por ejemplo, para Atalanta 22.4% y 94.7% son sus inclinaciones menores y mayores durante el torneo.

La descripción completa la encontrarás en la entrada [La inclinación del momento y la calidad de un equipo](https://www.nies.futbol/2024/06/la-inclinacion-del-momento-y-la-calidad.html).
"""

# Datos de ejemplo
st.subheader("Relación entre los indices de presión")
"""
En la figura de abajo podemos ver la relación que hay entre las variables de presión y otras
métricas.
Por ejemplo, podemos ver que entre los puntos logrados por un equipo (`pts`) y la calidad en el
momento (`quality`) hay una relación positiva.

También puedes ver que entre el índice gegenpressing (`ggpi`) y los pases permitidos por acción
defensiva (`ppda`) hay una relación inversa.
"""
path_josn = "static/datapackage.json"
f = open(path_josn)
data = json.load(f)
campos = data["resources"][0]["schema"]["fields"]
columns_to_choice = pressure.columns.drop(["id", "name"])
long_names = {
    campo["long_name"]: campo["name"] for campo in campos if campo["name"] in columns_to_choice
}
descriptions = {
    campo["long_name"]: campo["description"] for campo in campos if campo["name"] in columns_to_choice
}
columns_long_name = [llave for llave in long_names.keys()]
# Selección de variables x e y
x_long_name = st.selectbox("Selecciona la variable para el eje X", options=columns_long_name)
st.text(f"{x_long_name}: {descriptions[x_long_name]}")
y_long_name = st.selectbox("Selecciona la variable para el eje Y", options=columns_long_name)
st.text(f"{y_long_name}: {descriptions[y_long_name]}")

x_axis = long_names[x_long_name]
y_axis = long_names[y_long_name]
# Crear la gráfica de dispersión
scatter_plot = (
    alt.Chart(pressure)
    .mark_circle(size=60)
    .encode(
        x=alt.X(x_axis, title=x_long_name),
        y=alt.Y(y_axis, title=y_long_name),
        tooltip=[x_axis, y_axis, "name"],
    )
    .interactive()
)

# Crear la línea de tendencia
line = scatter_plot.transform_regression(x_axis, y_axis).mark_line(color="red")

# Combinar la gráfica de dispersión y la línea de tendencia
combined_chart = scatter_plot + line

# Agregar el logotipo en la esquina inferior izquierda
logo_url = "https://raw.githubusercontent.com/niesfutbol/hierarchical_review_mx/develop/static/logo_nies.png"
logo = (
    alt.Chart(
        pd.DataFrame(
            {"x": [pressure[x_axis].min()], "y": [pressure[y_axis].min()], "url": [logo_url]}
        )
    )
    .mark_image(width=50, height=50)
    .encode(
        x=alt.value(35), y=alt.value(250), url="url"  # Posición fija en x  # Posición fija en y
    )
)

# Combinar el gráfico y el logotipo
final_chart = combined_chart + logo

# Mostrar la gráfica en la app de Streamlit
st.altair_chart(final_chart, use_container_width=True)


st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
