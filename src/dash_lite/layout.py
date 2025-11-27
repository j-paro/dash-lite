import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify


def create_layout() -> dmc.Container:
    """
    Minimal single-page layout using Dash Mantine Components.

    - Top bar
    - Controls section
    - Output section
    """
    theme_switch = dmc.Switch(
        offLabel=DashIconify(
            icon="radix-icons:sun",
            width=15,
            color=dmc.DEFAULT_THEME["colors"]["yellow"][8],
        ),
        onLabel=DashIconify(
            icon="radix-icons:moon",
            width=15,
            color=dmc.DEFAULT_THEME["colors"]["yellow"][6],
        ),
        id="color-scheme-switch",
        persistence=True,
        checked=True,
        color="gray",
    )

    return dmc.Container(
        size="md",
        px="xl",
        py="xl",
        children=[
            dmc.Stack(
                gap="xl",
                children=[
                    # Header
                    dmc.Group(
                        justify="space-between",
                        align="flex-start",
                        children=[
                            dmc.Stack(
                                gap="xs",
                                children=[
                                    dmc.Title("dash-lite starter", order=1),
                                    dmc.Text(
                                        "A minimal Dash template with Mantine components.",
                                        c="gray",
                                        size="lg",
                                    ),
                                ],
                            ),
                            theme_switch,
                        ],
                    ),
                    # Controls Section
                    dmc.Paper(
                        shadow="xs",
                        p="lg",
                        radius="md",
                        withBorder=True,
                        children=[
                            dmc.Stack(
                                gap="md",
                                children=[
                                    dmc.Select(
                                        id="greeting-style",
                                        label="Choose a greeting style:",
                                        data=[
                                            "friendly",
                                            "formal",
                                            "short",
                                        ],
                                        value="friendly",
                                        clearable=False,
                                    ),
                                    dmc.TextInput(
                                        id="name-input",
                                        label="Your name:",
                                        placeholder="Type your name",
                                        value="Friend",
                                    ),
                                ],
                            ),
                        ],
                    ),
                    # Output Section
                    dmc.Paper(
                        shadow="xs",
                        p="lg",
                        radius="md",
                        withBorder=True,
                        children=[
                            dmc.Stack(
                                gap="md",
                                children=[
                                    dmc.Title("Preview", order=2),
                                    html.Div(id="greeting-output"),
                                ],
                            ),
                        ],
                    ),
                    # Footer
                    dmc.Center(
                        children=[
                            dmc.Text(
                                "Built with dash-lite • Mantine Edition",
                                size="sm",
                                c="gray",
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )
