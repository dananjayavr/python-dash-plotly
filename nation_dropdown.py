from dash import Dash, html, dcc
from dash.dependencies import Input, Output

from ids import NATION_DROPDOWN, SELECT_ALL_NATIONS

def render(app: Dash) -> html.Div:
    all_nations = ["South Korea","China","Canada"]

    @app.callback(
        Output(NATION_DROPDOWN,"value"),
        Input(SELECT_ALL_NATIONS,"n_clicks")
    )
    def select_all_nations(_: int) -> list[str]:
        return all_nations

    return html.Div(
        children=[
            html.H6("Nation"),
            dcc.Dropdown(
                options=[{"label": nation, "value": nation} for nation in all_nations],
                value=all_nations,
                multi=True,
                id=NATION_DROPDOWN
            ),
            html.Button(
                className="dropdown-button",
                children=[
                    "Select All"
                ],
                id=SELECT_ALL_NATIONS
            )
        ]
    )