# dash-lite – AI Coding Agent Instructions

## Project Overview

**dash-lite** is a minimal Dash starter template with three parallel implementations demonstrating different styling approaches:
- `dash_lite/` - Vanilla Dash with custom CSS
- `using_tailwind/` - Tailwind CSS (CDN) with native HTML components
- `using_dmc/` - Dash Mantine Components

Each implementation follows identical structure: `app.py` (entry point), `layout.py` (UI), `callbacks.py` (interactivity).

## General Guidelines

Don't do anything to the code in the `deprecated/` folder. It contains legacy versions kept for reference only. Also, don't create any code that pertains to the deprecated versions.

## Critical Architecture Patterns

### Multi-Implementation Structure
All three apps are **independent, parallel implementations** in `src/`. They share:
- Identical callback logic (`_build_greeting` function)
- Same environment variable patterns (`DASH_LITE_PORT`, `DASH_LITE_DEBUG`)
- Similar project structure (app factory, layout separation, callback registration)

When modifying one implementation, **do not automatically update others** unless explicitly requested.

### App Factory Pattern
Each `app.py` uses:
```python
def create_app() -> Dash:
    app = Dash(__name__, ...)
    app.layout = create_layout()
    register_callbacks(app)
    return app
```

### Port Assignments
- `dash_lite`: 8050 (default)
- `using_tailwind`: 8051
- `using_dmc`: 8052

## Technology-Specific Conventions

### Dash Mantine Components (`using_dmc/`)
- **Always wrap layout in `dmc.MantineProvider`**
- Follow `.github/instructions/dmc.instructions.md` for component usage
- Use `dmc.Stack`, `dmc.Group`, `dmc.Paper` for layouts (not raw HTML)
- Prefer DMC's built-in theming over custom CSS
- Font weight: Use string literals (`"bold"`) not numbers (`500`)

### Tailwind (`using_tailwind/`)
- CDN loaded via `external_scripts` in Dash constructor
- Use **native HTML components** (`html.Select`, `html.Input`) not `dcc` components
- Tailwind utility classes go in `className` prop
- Minimal custom CSS in `assets/` (only for Dash component overrides)

### Vanilla Dash (`dash_lite/`)
- Uses `dcc.Dropdown`, `dcc.Input` standard components
- All styling in `assets/styles.css`
- Fallback/reference implementation

## Development Workflows

### Running Apps
```powershell
poetry install                    # Install dependencies
poetry run dashlite              # Run main app (dash_lite)
poetry run python -m using_dmc.app       # Run DMC version
poetry run python -m using_tailwind.app  # Run Tailwind version
```

### Key Dependencies
- `dash` >= 3.3.0 - Core framework
- `dash-mantine-components` >= 2.4.0 - Optional (DMC version only)
- Python >= 3.13

### Entry Points
Defined in `pyproject.toml`:
```toml
[project.scripts]
dashlite = "dash_lite.app:main"
```

## Code Quality Standards

### Modern Dash Patterns (REQUIRED)
- Use `ctx` instead of deprecated `callback_context`
- Callback inputs as individual arguments, **not lists**:
  ```python
  @app.callback(Output(...), Input(...), Input(...))  # ✓ Correct
  @app.callback(Output(...), [Input(...), Input(...)])  # ✗ Wrong
  ```
- Use `ctx.triggered_id` for trigger detection

### Python Conventions
Follow `.github/instructions/python.instructions.md`:
- Type hints on all functions
- Docstrings in PEP 257 format
- PEP 8 formatting (4 spaces, 79 char lines)
- Descriptive function names

### Styling Philosophy
- **DMC**: Zero custom CSS, use component props + theme
- **Tailwind**: Utility-first classes, minimal CSS overrides
- **Vanilla**: Clean, semantic CSS classes

## Common Pitfalls

1. **Don't mix styling approaches** - Each implementation uses ONE method exclusively
2. **Don't add Tailwind to DMC** - They're mutually exclusive design systems
3. **Callback imports** - Never use old patterns like `callback_context.triggered[0]`
4. **DMC wrapper** - Must wrap entire layout in `MantineProvider`, not individual sections
5. **Tailwind + dcc components** - Won't work well; use native HTML instead

## Project-Specific Context

### Why Three Implementations?
Demonstrates trade-offs between:
- Full control (vanilla CSS)
- Utility-first rapid development (Tailwind)
- Component library convenience (DMC)

### File You Should Reference
- `.github/instructions/dmc.instructions.md` - Comprehensive DMC component reference (~50K lines)
- `.github/instructions/project_plan.instructions.md` - High-level goals and non-goals
- `pyproject.toml` - Dependencies and entry points

### When Making Changes
1. **Read the plan** - Check if request aligns with project goals (simplicity, minimal scope)
2. **Check instructions** - DMC components have specific prop requirements
3. **Preserve parallelism** - Changes to one implementation shouldn't break others
4. **Test locally** - Verify the app runs on correct port with `poetry run`

## Questions to Ask User

When unclear about:
- Which implementation to modify (dash_lite vs using_dmc vs using_tailwind)
- Whether to sync changes across all implementations
- If a feature request fits the "minimal starter" philosophy
- Styling approach preferences for new components
