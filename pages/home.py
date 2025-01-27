#home.py

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
dash.register_page(__name__, path="/")

layout = html.Div(
    [
        # -- HERO SECTION --
        html.Div(
            className="hero-section d-flex align-items-center justify-content-center text-center",
            children=[
                html.Div(className="hero-overlay"),
                html.Div(
                    className="hero-content",
                    children=[
                        html.Img(
                            src="/assets/images/profile.jpg",
                            className="profile-pic mb-3"
                        ),
                        html.H1(
                            "Aryan D. Khedkar",
                            className="hero-title"
                        ),
                        html.P(
                            "Imperial Physics Graduate | FinTech Entrepreneur | Business Intelligence ML Analyst",
                            className="hero-subtitle"
                        ),
                        # New vision statement
                        html.P(
                            "Combining Human Ingenuity with Machine Intelligence "
                            ,
                            className="vision-text mt-4"
                        ),
                        dbc.Button(
                            "View My Work",
                            href="/higheryou",
                            color="primary",
                            className="mt-3 hero-cta-btn btn-lg"
                        )
                    ]
                ),
            ],
        ),



           # -- SNAPSHOT SECTION --
html.Div(
    className="experience-section",  # <-- new wrapper
    children=[
        dbc.Container(
            [
                html.H2(
                    "Snapshot of My Experience",
                    className="mt-2 mb-3 text-center"
                ),
                html.P(
                    """
                    Born in a small Indian town with scorching summers and lively academic debates,
                    I pursued Physics at Imperial College London to blend rigorous science 
                    with real-world problem-solving.

                    Certified in Data Analytics (Google), Business Intelligence, 
                    and Deep Learning (Stanford & DeepLearning.AI), 
                    I thrive on converting complex data into sustainable, high-impact solutions.

                    With a passion for scaling innovation at the crossroads of tech, 
                    entrepreneurship, and social good, I’m committed to helping others 
                    reach their goals without losing sight of their values.
                    """,
                    className="mt-3 mb-3 text-center"
                    # text-white => text color white
                    # mb-5 => larger bottom margin
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader("Physics at Imperial"),
                                    dbc.CardBody(
                                        html.P(
                                            "Gained a robust grounding in theoretical and applied physics, "
                                            "fueling my passion for bridging academia and industry."
                                        )
                                    ),
                                    dbc.CardLink("View Projects", href="/higheryou", className="stretched-link")
                                ],
                                className="card-item text-center mb-3",
                                style={"cursor": "pointer"}
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader("Data Analytics & BI"),
                                    dbc.CardBody(
                                        html.P(
                                            "Certified by Google, skilled in translating raw data "
                                            "into strategic insights and intuitive dashboards."
                                        )
                                    ),
                                    dbc.CardLink("View Projects", href="/higheryou", className="stretched-link")
                                ],
                                className="card-item text-center mb-3",
                                style={"cursor": "pointer"}
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader("Deep Learning Specialization"),
                                    dbc.CardBody(
                                        html.P(
                                            "Completed advanced AI coursework with Stanford & DeepLearning.AI, "
                                            "applying ML techniques to real-world challenges."
                                        )
                                    ),
                                    dbc.CardLink("View Projects", href="/higheryou", className="stretched-link")
                                ],
                                className="card-item text-center mb-3",
                                style={"cursor": "pointer"}
                            )
                        )
                    ],
                    justify="center"
                ),
            ],
            fluid=True
        ),
    ],
)
])