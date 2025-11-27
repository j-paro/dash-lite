from __future__ import annotations

import os

import dash_mantine_components as dmc
from dash import Dash, Input, Output, clientside_callback

from .callbacks import register_callbacks
from .layout import create_layout


def create_app() -> Dash:
    """
    Create and configure a minimal Dash app with Dash Mantine Components.

    This version uses DMC for a modern, beautiful UI without custom CSS.
    """
    app = Dash(
        __name__,
        title="dash-lite starter (Mantine)",
        suppress_callback_exceptions=False,
    )

    app.layout = dmc.MantineProvider(
        create_layout(),
        defaultColorScheme="dark",
    )
    register_callbacks(app)

    # Theme switch callback
    clientside_callback(
        """
        (switchOn) => {
           document.documentElement.setAttribute('data-mantine-color-scheme', switchOn ? 'dark' : 'light');
           return window.dash_clientside.no_update
        }
        """,
        Output("color-scheme-switch", "id"),
        Input("color-scheme-switch", "checked"),
    )

    return app


def main() -> None:
    """Entry point for the Mantine version."""
    app = create_app()

    port = int(os.getenv("DASH_LITE_PORT", "8052"))
    debug = os.getenv("DASH_LITE_DEBUG", "true").lower() == "true"

    app.run(host="0.0.0.0", port=port, debug=debug)


if __name__ == "__main__":
    main()
