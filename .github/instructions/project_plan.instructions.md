# dash-lite – Project Plan & Copilot Instructions

## 1. Project Overview

**dash-lite** is a minimal, opinionated Dash starter app.

It is intentionally small and focused:

- Single-page Dash app
- Clean layout with header, controls, and output area
- One or two simple example callbacks
- Ready to run via a console script (e.g., `dash-lite`) or `python -m dash_lite_app`
- Easy for others to clone and adapt as a starting point for their own Dash apps

The project should favor **clarity and simplicity** over advanced features. It is an open source “starter kit,” not a full framework.

---

## 2. Goals & Non-Goals

### 2.1 Goals

- Provide a **minimal, well-structured** Dash project template.
- Demonstrate:
  - A clean layout (header, controls, output)
  - At least one meaningful callback (input → output)
- Make it easy to:
  - Install with `pip`
  - Run locally with a single command
  - Understand the structure in under 5 minutes
- Be **simple enough** for beginners but **not** toy-quality.

### 2.2 Non-Goals (for early versions)

Copilot should **avoid** adding any of these unless explicitly requested:

- Authentication / authorization
- Database integrations
- Multi-page routing or complex navigation
- State management beyond simple callbacks
- Docker, CI/CD, or deployment configs
- Frontend frameworks beyond Dash + basic CSS (Tailwind will come in a later milestone)

---

## 3. Tech Stack & Conventions

- **Language:** Python (3.10+)
- **Framework:** [Plotly Dash](https://dash.plotly.com/)
- **Packaging:** `pyproject.toml` with `setuptools`
- **Entry point:** console script `dash-lite` and `python -m dash_lite_app`
- **Styling:**
  - v0.1 – simple CSS in `assets/styles.css`
  - v0.2 – Tailwind CSS via a build step (precompiled into `assets/styles.css`)
- **Code style:**
  - Prefer type hints
  - Keep functions small and focused
  - Separate layout and callbacks into different modules

---

## 4. Project Structure

Target structure:

```text
dash-lite/
  DASH_LITE_PLAN.md
  README.md
  pyproject.toml
  src/
    dash_lite_app/
      __init__.py
      app.py         # app factory + main entry point
      layout.py      # defines Dash layout
      callbacks.py   # registers callbacks
      assets/
        styles.css   # compiled CSS (plain for v0.1, Tailwind later)
        # tailwind.css (source, introduced in v0.2)
