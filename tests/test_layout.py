"""Tests for the layout module."""

from __future__ import annotations

import dash_mantine_components as dmc

from dash_lite.layout import create_layout


def test_create_layout_returns_appshell() -> None:
    """Test that create_layout returns an AppShell component."""
    layout = create_layout()

    assert isinstance(layout, dmc.AppShell)


def test_layout_has_required_components() -> None:
    """Test that layout contains all required interactive components."""
    layout = create_layout()

    # Helper function to find components by ID in component tree
    def find_component_by_id(component, target_id: str) -> bool:
        """Recursively search for a component with given ID."""
        # Check if component has an id attribute
        if hasattr(component, "id") and component.id == target_id:
            return True

        # Check if component has children
        if hasattr(component, "children"):
            children = component.children
            if children:
                if isinstance(children, list):
                    return any(
                        find_component_by_id(child, target_id)
                        for child in children
                    )
                else:
                    return find_component_by_id(children, target_id)
        return False

    # Check for required component IDs
    assert find_component_by_id(layout, "greeting-style")
    assert find_component_by_id(layout, "name-input")
    assert find_component_by_id(layout, "greeting-output")
    assert find_component_by_id(layout, "color-scheme-switch")
    assert find_component_by_id(layout, "burger-button")
    assert find_component_by_id(layout, "app-shell")


def test_layout_greeting_style_has_correct_options() -> None:
    """Test that greeting style Select has correct options."""
    layout = create_layout()

    def find_select_data(component) -> list | None:
        """Find the Select component's data."""
        # Check if this is the greeting-style component
        if (
            hasattr(component, "id")
            and component.id == "greeting-style"
            and hasattr(component, "data")
        ):
            return component.data

        # Check children
        if hasattr(component, "children"):
            children = component.children
            if children:
                if isinstance(children, list):
                    for child in children:
                        result = find_select_data(child)
                        if result:
                            return result
                else:
                    return find_select_data(children)
        return None

    select_data = find_select_data(layout)
    assert select_data == ["friendly", "formal", "short"]


def test_layout_has_default_values() -> None:
    """Test that input components have appropriate default values."""
    layout = create_layout()

    def find_component_value(component, target_id: str) -> str | None:
        """Find a component's value by ID."""
        # Check if this is the target component
        if (
            hasattr(component, "id")
            and component.id == target_id
            and hasattr(component, "value")
        ):
            return component.value

        # Check children
        if hasattr(component, "children"):
            children = component.children
            if children:
                if isinstance(children, list):
                    for child in children:
                        result = find_component_value(child, target_id)
                        if result is not None:
                            return result
                else:
                    return find_component_value(children, target_id)
        return None

    # Check default values
    assert find_component_value(layout, "greeting-style") == "friendly"
    assert find_component_value(layout, "name-input") == "Friend"
