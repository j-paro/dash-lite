"""Tests for the callbacks module."""

from __future__ import annotations

from dash import Dash

from dash_lite.callbacks import _build_greeting, register_callbacks


class TestBuildGreeting:
    """Tests for the _build_greeting helper function."""

    def test_friendly_greeting(self) -> None:
        """Test friendly greeting style."""
        result = _build_greeting("friendly", "Alice")
        assert result == "Hey Alice, welcome to dash-lite! 👋"

    def test_formal_greeting(self) -> None:
        """Test formal greeting style."""
        result = _build_greeting("formal", "Bob")
        assert result == "Hello, Bob. It's a pleasure to meet you."

    def test_short_greeting(self) -> None:
        """Test short greeting style."""
        result = _build_greeting("short", "Charlie")
        assert result == "Hi, Charlie!"

    def test_empty_name_uses_default(self) -> None:
        """Test that empty name falls back to 'Friend'."""
        result = _build_greeting("friendly", "")
        assert result == "Hey Friend, welcome to dash-lite! 👋"

    def test_whitespace_name_uses_default(self) -> None:
        """Test that whitespace-only name falls back to 'Friend'."""
        result = _build_greeting("friendly", "   ")
        assert result == "Hey Friend, welcome to dash-lite! 👋"

    def test_name_with_whitespace_is_trimmed(self) -> None:
        """Test that names with surrounding whitespace are trimmed."""
        result = _build_greeting("short", "  Dana  ")
        assert result == "Hi, Dana!"

    def test_unknown_style_defaults_to_friendly(self) -> None:
        """Test that unknown style falls back to friendly."""
        result = _build_greeting("unknown", "Eve")
        assert result == "Hey Eve, welcome to dash-lite! 👋"


def test_register_callbacks_adds_callbacks_to_app() -> None:
    """Test that register_callbacks adds callbacks to the Dash app."""
    app = Dash(__name__)

    # Initially no callbacks
    initial_count = len(app.callback_map)

    register_callbacks(app)

    # Should have at least one callback registered
    assert len(app.callback_map) > initial_count


def test_greeting_callback_is_registered(dash_app: Dash) -> None:
    """Test that the greeting callback is properly registered."""
    callback_id = "greeting-output.children"
    callback = dash_app.callback_map.get(callback_id)

    assert callback is not None
    assert len(callback["inputs"]) == 2
    assert callback["inputs"][0]["id"] == "greeting-style"
    assert callback["inputs"][1]["id"] == "name-input"
