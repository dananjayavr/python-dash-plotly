from dash import Dash, html
from layout import cerate_layout
from dash_bootstrap_components.themes import BOOTSTRAP

def main() -> None:
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Medal Dashboard"
    app.layout = cerate_layout(app)
    app.run()

if __name__ == "__main__":
    main()