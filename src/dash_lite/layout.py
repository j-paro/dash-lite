import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify


def create_layout() -> dmc.AppShell:
    """
    Dashboard layout using AppShell with header, navbar, footer, and main content.

    Responsive design that collapses navbar on mobile devices.
    """
    # Theme toggle switch
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

    # Header content
    header = dmc.AppShellHeader(
        dmc.Group(
            justify="space-between",
            align="center",
            h="100%",
            px="md",
            children=[
                dmc.Group(
                    gap="sm",
                    children=[
                        dmc.Burger(
                            id="burger-button",
                            opened=False,
                            hiddenFrom="sm",
                            size="sm",
                        ),
                        dmc.Title("dash-lite", order=3, c="blue"),
                    ],
                ),
                theme_switch,
            ],
        ),
    )

    # Navbar/Sidebar content
    navbar = dmc.AppShellNavbar(
        p="md",
        children=[
            dmc.Stack(
                gap="sm",
                children=[
                    dmc.Text("Navigation", fw="bold", size="sm", c="gray"),
                    dmc.NavLink(
                        label="Dashboard",
                        leftSection=DashIconify(icon="tabler:home", width=20),
                        variant="filled",
                    ),
                    dmc.NavLink(
                        label="Analytics",
                        leftSection=DashIconify(
                            icon="tabler:chart-bar", width=20
                        ),
                    ),
                    dmc.NavLink(
                        label="Settings",
                        leftSection=DashIconify(
                            icon="tabler:settings", width=20
                        ),
                    ),
                    dmc.Divider(my="sm"),
                    dmc.Text("Demo Controls", fw="bold", size="sm", c="gray"),
                ],
            ),
        ],
    )

    # Main content area
    main_content = dmc.AppShellMain(
        dmc.Container(
            size="xl",
            py="xl",
            children=[
                dmc.Stack(
                    gap="xl",
                    children=[
                        # Page header
                        dmc.Stack(
                            gap="xs",
                            children=[
                                dmc.Title(
                                    "Welcome to Your Dashboard", order=1
                                ),
                                dmc.Text(
                                    "A flexible, responsive starter template with header, sidebar, and footer",
                                    size="lg",
                                    c="gray",
                                ),
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
                                        dmc.Title(
                                            "Interactive Demo",
                                            order=2,
                                            size="h3",
                                        ),
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
                                        dmc.Title(
                                            "Preview", order=2, size="h3"
                                        ),
                                        html.Div(id="greeting-output"),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    )

    # Footer content
    footer = dmc.AppShellFooter(
        p="md",
        children=dmc.Group(
            justify="space-between",
            children=[
                dmc.Text(
                    "Built with dash-lite • Mantine Edition",
                    size="sm",
                    c="gray",
                ),
                dmc.Group(
                    gap="xs",
                    children=[
                        dmc.ActionIcon(
                            DashIconify(icon="tabler:brand-github", width=20),
                            variant="subtle",
                            color="gray",
                            size="lg",
                        ),
                        dmc.ActionIcon(
                            DashIconify(icon="tabler:help", width=20),
                            variant="subtle",
                            color="gray",
                            size="lg",
                        ),
                    ],
                ),
            ],
        ),
    )

    # AppShell with responsive configuration
    return dmc.AppShell(
        [
            header,
            navbar,
            main_content,
            footer,
        ],
        id="app-shell",
        header={"height": 60},
        navbar={
            "width": 250,
            "breakpoint": "sm",
            "collapsed": {"mobile": True},
        },
        footer={"height": 60},
        padding="md",
    )
