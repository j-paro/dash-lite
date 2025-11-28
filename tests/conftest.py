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
