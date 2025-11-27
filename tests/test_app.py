"""Tests for the main application module."""

from __future__ import annotations

import dash_mantine_components as dmc
from dash import Dash

from dash_lite.app import create_app


def test_create_app_returns_dash_instance() -> None:
    """Test that create_app returns a Dash instance."""
    app = create_app()

    assert isinstance(app, Dash)
    assert app.title == "dash-lite starter (Mantine)"


def test_app_has_layout(dash_app: Dash) -> None:
    """Test that the app has a layout configured."""
    assert dash_app.layout is not None


def test_app_layout_wrapped_in_mantine_provider(dash_app: Dash) -> None:
    """Test that layout is wrapped in MantineProvider."""
    assert isinstance(dash_app.layout, dmc.MantineProvider)


def test_app_has_callbacks_registered(dash_app: Dash) -> None:
    """Test that callbacks are registered on the app."""
    # Check that callbacks are registered
    assert len(dash_app.callback_map) > 0


def test_app_suppress_callback_exceptions(dash_app: Dash) -> None:
    """Test that suppress_callback_exceptions is set correctly."""
    assert dash_app.config.suppress_callback_exceptions is False
