# dash-lite

A minimal Dash starter template demonstrating modern Python best practices with a clean, production-ready structure.

## Project Status

**Current Implementation:** Single production-ready app using Dash Mantine Components (DMC)

- **Active:** `src/dash_lite/` - DMC-based implementation with dark/light theme switching

This project has consolidated to focus on the DMC implementation as the primary, maintained version.

## Features

- 🎨 **Modern UI** with Dash Mantine Components
- 🌓 **Dark/Light Theme** switching with persistence
- 🏗️ **Clean Architecture** using app factory pattern
- 📦 **Type-Safe** with full type hints
- 🚀 **Production-Ready** with environment variable configuration

## Quick Start

### Prerequisites

- Python >= 3.13
- Poetry (recommended) or pip

### Installation

```powershell
# Clone the repository
git clone https://github.com/yourusername/dash-lite.git
cd dash-lite

# Install dependencies with Poetry
poetry install

# Or with pip
pip install -e .
```

### Running the App

```powershell
# Using the entry point
poetry run dashlite

# Or directly
poetry run python -m dash_lite.app
```

The app will start on `http://localhost:8052` by default.

### Configuration

Control app behavior via environment variables:

- `DASH_LITE_PORT` - Server port (default: `8052`)
- `DASH_LITE_DEBUG` - Debug mode (default: `true`)

```powershell
# Example: Run on different port
$env:DASH_LITE_PORT="9000"; poetry run dashlite
```

## Project Structure

```
dash-lite/
├── src/
│   └── dash_lite/           # Main application
│       ├── __init__.py
│       ├── app.py           # App factory & entry point
│       ├── layout.py        # UI component structure
│       └── callbacks.py     # Interactive logic
├── deprecated/              # Legacy implementations (not maintained)
│   ├── original/            # Vanilla Dash + CSS
│   └── using_tailwind/      # Tailwind CSS version
├── .github/
│   ├── copilot-instructions.md
│   └── instructions/        # Coding standards & guides
├── pyproject.toml           # Dependencies & config
└── README.md
```

## Architecture

### App Factory Pattern

Each module follows a clean separation of concerns:

**`app.py`** - Application creation and configuration
```python
def create_app() -> Dash:
    """Create and configure the Dash app."""
    app = Dash(__name__, title="dash-lite starter (Mantine)")
    app.layout = dmc.MantineProvider(create_layout())
    register_callbacks(app)
    return app
```

**`layout.py`** - UI component structure
- Pure layout definition
- No callback logic
- DMC components wrapped in `MantineProvider`

**`callbacks.py`** - Interactive behavior
```python
def register_callbacks(app: Dash) -> None:
    """Register all callback functions."""
    @app.callback(...)
    def update_greeting(...):
        ...
```

### Modern Dash Patterns

This template uses current Dash best practices:

- ✅ `ctx.triggered_id` for trigger detection (not deprecated `callback_context`)
- ✅ Individual callback inputs as arguments (not lists)
- ✅ Type hints on all functions
- ✅ Clientside callbacks for performance
- ✅ Component state persistence

## Dependencies

Core dependencies (from `pyproject.toml`):

- **dash** >= 3.3.0 - Core framework
- **dash-mantine-components** >= 2.4.0 - UI component library
- **dash-iconify** >= 0.1.2 - Icon support

## Development

### Code Quality Standards

This project follows:

- **PEP 8** formatting (4 spaces, 79 char lines)
- **PEP 257** docstring conventions
- **Type hints** on all functions
- **Modern Dash patterns** (see `.github/instructions/python.instructions.md`)

### Testing

See [tests/README.md](tests/TESTING.md) for information on running tests and test coverage.

### Development Tools

See [TOOLS.md](TOOLS.md) for available development tools and utilities

### DMC Conventions

When working with Dash Mantine Components:

- Always wrap layout in `dmc.MantineProvider`
- Use DMC layout components (`dmc.Stack`, `dmc.Group`, `dmc.Paper`)
- Leverage built-in theming instead of custom CSS
- String literals for font weights (`"bold"` not `500`)

See `.github/instructions/dmc.instructions.md` for comprehensive component reference.

## Example Application

The included demo app showcases:

1. **Component Selection** - `dmc.Select` dropdown for greeting styles
2. **Text Input** - `dmc.TextInput` with validation
3. **Dynamic Output** - Callback-driven content updates
4. **Theme Switching** - Persistent dark/light mode toggle
5. **Responsive Layout** - Container-based structure

## Deprecated Implementations

The `deprecated/` folder contains two earlier implementations kept for reference:

- **`original/`** - Vanilla Dash with custom CSS (port 8050)
- **`using_tailwind/`** - Tailwind CSS via CDN (port 8051)

These are **not maintained** and may have outdated patterns. Refer to them only for architectural comparison.

## Philosophy

**dash-lite** prioritizes:

- ✨ **Simplicity** - Minimal dependencies, clear structure
- 📚 **Education** - Demonstrates best practices
- 🚀 **Speed** - Get building quickly
- 🔧 **Flexibility** - Easy to extend or strip down

This is **not**:
- ❌ A full-featured dashboard framework
- ❌ An opinionated state management system
- ❌ A component showcase (see Mantine docs for that)

## License

MIT

## Contributing

This is a starter template. Fork it and make it your own!

For AI coding assistants working on this project, see `.github/copilot-instructions.md` for architecture guidelines and patterns.
