import pytest
import pandas as pd
import altair as alt
import pression_index_st as pis


@pytest.fixture
def sample_data():
    return pd.DataFrame(
        {"A": [1, 2, 3, 4, 5], "B": [2, 3, 2, 5, 7], "C": [5, 4, 3, 2, 1], "D": [7, 8, 7, 9, 10]}
    )


def test_scatter_plot_creation(sample_data):
    x_axis = "A"
    y_axis = "B"
    chart = pis.create_scatter_plot(sample_data, x_axis, y_axis)

    # Verifica que el gráfico es una instancia de alt.Chart
    assert isinstance(chart, alt.Chart), "El gráfico debe ser una instancia de alt.Chart"

    # Verifica que el gráfico contiene los datos correctos
    assert chart.encoding.x.shorthand == x_axis, f"El eje X debe ser {x_axis}"
    assert chart.encoding.y.shorthand == y_axis, f"El eje Y debe ser {y_axis}"

    # Verifica que la marca es de tipo círculo
    assert chart.mark.type == "circle", "La marca del gráfico debe ser de tipo círculo"

    # Verifica que el tamaño del círculo es correcto
    assert chart.mark.size == 60, "El tamaño del círculo debe ser 60"

    # Verifica que la interactividad está habilitada
    assert chart.interactive(), "El gráfico debe ser interactivo"
