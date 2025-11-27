"""Pytest configuration and shared fixtures."""

from __future__ import annotations

import pytest
from dash import Dash


@pytest.fixture
def dash_app() -> Dash:
    """
    Create a Dash app instance for testing.

    Returns:
        Configured Dash application instance.
    """
    from dash_lite.app import create_app

    app = create_app()
    return app


@pytest.fixture
def dash_duo(dash_duo):
    """
    Provide Dash testing duo with common configuration.

    This fixture wraps the dash_duo fixture from dash.testing
    with any project-specific configuration.
    """
    # Set default wait time for components to load
    dash_duo.wait_for_page(timeout=10)
    return dash_duo
