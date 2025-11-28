import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, ctx


def _build_greeting(style: str, name: str) -> str:
    name = name.strip() or "Friend"

    if style == "formal":
        return f"Hello, {name}. It's a pleasure to meet you."
    if style == "short":
        return f"Hi, {name}!"
    return f"Hey {name}, welcome to dash-lite! 👋"


def register_callbacks(app: Dash) -> None:
    """Register all application callbacks."""

    @app.callback(
        Output("greeting-output", "children"),
        Input("greeting-style", "value"),
        Input("name-input", "value"),
    )
    def update_greeting(style: str, name: str) -> dmc.Text:
        # Minimal example: one clear transformation from inputs → output
        trigger = ctx.triggered_id if ctx.triggered_id else "initial-load"

        greeting = _build_greeting(style, name or "")

        return dmc.Text(
            greeting,
            size="lg",
            fw="bold",
            **{"data-triggered-by": trigger},  # type: ignore
        )

    @app.callback(
        Output("burger-button", "opened"),
        Output("app-shell", "navbar"),
        Input("burger-button", "n_clicks"),
        State("app-shell", "navbar"),
    )
    def toggle_navbar(n_clicks: int, navbar: dict) -> tuple[bool, dict]:
        """Toggle the navbar collapsed state when burger button is clicked."""
        if n_clicks:
            # Toggle the mobile collapsed state
            opened = not navbar["collapsed"]["mobile"]
            navbar["collapsed"]["mobile"] = not opened
            return opened, navbar
        return False, navbar
