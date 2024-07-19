import altair as alt


def create_scatter_plot(data, x_axis, y_axis):
    scatter_plot = (
        alt.Chart(data)
        .mark_circle(size=60)
        .encode(x=x_axis, y=y_axis, tooltip=[x_axis, y_axis])
        .interactive()
    )

    return scatter_plot
