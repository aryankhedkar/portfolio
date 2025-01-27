# app.py

import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from dash import Input, Output, State


# ------------------------------------------------------------------------------
# 1. INITIALIZE APP WITH CUSTOM index_string
# ------------------------------------------------------------------------------
#
# We embed your original <meta> tags, <title>, and Google Font link 
# in app.index_string. Dash replaces {%css%}, {%config%}, {%scripts%}, 
# and {%renderer%} with its own content.

app = Dash(
    __name__,
    use_pages=True,  # for multi-page support
    external_stylesheets=[dbc.themes.BOOTSTRAP], 
    suppress_callback_exceptions=True
)
server = app.server  # For deployment (e.g., on Heroku)

# ------------------------------------------------------------------------------
# 2. NAVIGATION BAR
# ------------------------------------------------------------------------------
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("Aryan D. Khedkar", className="navbar-brand"),

            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/", active="exact", className="nav-link mx-2"),
                    #dbc.NavLink("Projects", href="/projects", active="exact", className="nav-link mx-2"),
                    dbc.NavLink("Higher You", href="/higheryou", active="exact", className="nav-link mx-2"),
                    dbc.NavLink("Writing", href="/writing", active="exact", className="nav-link mx-2"),
                    dbc.NavLink("My Story", href="/about_me", active="exact", className="nav-link mx-2"),
                    dbc.NavLink("Connect", href="/connect", active="exact", className="nav-link mx-2"),
                ],
                navbar=True,
                className="ms-auto"
            ),
        ],
        fluid=True
    ),
    color="black",
    dark=True,
    sticky="top",
    className="mb-4"
)

# ------------------------------------------------------------------------------
# 3. FOOTER
# ------------------------------------------------------------------------------
footer = html.Footer(
    dbc.Container(
        [
            html.Hr(className="bg-secondary"),
            html.P(
                [
                    "© 2025 Aryan D. Khedkar | ",
                    html.Span("Guided by Truth, Courage and Love, I aim to strive towards the Ideal of Innovation.")
                ],
                className="m-0 text-center text-white"
            ),
            html.Div(
                [
                    html.A(
                        "LinkedIn",
                        href="https://www.linkedin.com/in/aryankhedkar0000/",
                        target="_blank",
                        className="footer-link mx-2"
                    ),
                    html.A(
                        "X (Twitter)",
                        href="https://x.com/AryanK_0000",
                        target="_blank",
                        className="footer-link mx-2"
                    ),
                    html.A(
                        "YouTube",
                        href="https://www.youtube.com/@aryankhedkar0000",
                        target="_blank",
                        className="footer-link mx-2"
                    ),
                ],
                className="text-center mt-3"
            ),
        ],
        fluid=True,
        className="py-4"
    ),
    style={"backgroundColor": "black"}
)

# ------------------------------------------------------------------------------
# 4. APP LAYOUT
# ------------------------------------------------------------------------------
app.layout = html.Div([
    navbar,
    dash.page_container,
    footer
])

# ------------------------------------------------------------------------------
# 5. CALLBACK FOR CONTACT FORM
# ------------------------------------------------------------------------------
@app.callback(
    Output("contact-feedback", "children"),
    Input("contact-submit", "n_clicks"),
    State("contact-name", "value"),
    State("contact-email", "value"),
    State("contact-message", "value")
)
def handle_form(n_clicks, name, email, message):
    if n_clicks > 0:
        # Example: you might send an email or store to a database here
        return (
            "Thanks, truly. The fact that you spent a few min of your day to "
            "reach out to me means a lot to me. I'll get back to you asap."
        )
    return ""

# ------------------------------------------------------------------------------
# 6. RUN SERVER
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run_server(debug=True)
