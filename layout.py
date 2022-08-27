from dash import Dash, html
import bar_chart
import nation_dropdown


def cerate_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    nation_dropdown.render(app)
                ]
            ),
            bar_chart.render(app)
        ]
    )