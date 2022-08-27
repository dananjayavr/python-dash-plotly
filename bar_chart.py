from dash import Dash, dcc, html
import plotly.express as px
from dash.dependencies import Input, Output

from ids import BAR_CHART, NATION_DROPDOWN

MEDAL_DATA = px.data.medals_long()

def render(app: Dash) -> html.Div :
    @app.callback(
        Output(BAR_CHART,"children"),
        Input(NATION_DROPDOWN,"value")
    )
    def update_bar_chart(nations: list[str]) -> html.Div:
        filtered_data = MEDAL_DATA.query("nation in @nations")
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.")

        fig = px.bar(filtered_data,x="medal",y="count",color="nation",text="nation")
        return html.Div(dcc.Graph(figure=fig),id=BAR_CHART)
    
    return html.Div(id=BAR_CHART)
