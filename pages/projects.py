# pages/projects.py
import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/higheryou")


layout = html.Div([

    # HEADER
    html.Header([
        html.Div([
            html.Div("Higher You", className="logo"),
            html.Nav(
                html.Ul([
                    html.Li(html.A("About", href="#About")),
                    html.Li(html.A("Value", href="#Value")),
                    html.Li(html.A("Testimonials", href="#testimonials")),
                    html.Li(html.A("Pricing", href="#pricing")),
                    #html.Li(html.A("Contact", href="#contact")),
                ])
            ),
            # Hamburger for mobile
            html.Div(
                [
                    html.Div(className="bar"),
                    html.Div(className="bar"),
                    html.Div(className="bar"),
                ],
                className="hamburger",
                id="hamburger"
            )
        ], className="header-container"),

        # Mobile nav menu
        html.Div([
            html.Ul([
                html.Li(html.A("About", href="#About", **{"data-toggle-nav": "true"})),
                html.Li(html.A("Value", href="#Value", **{"data-toggle-nav": "true"})),
                html.Li(html.A("Testimonials", href="#testimonials", **{"data-toggle-nav": "true"})),
                html.Li(html.A("Pricing", href="#pricing", **{"data-toggle-nav": "true"})),
                #html.Li(html.A("Contact", href="#contact", **{"data-toggle-nav": "true"})),
            ])
        ], className="mobile-nav", id="mobileNav")
    ]),

    # HERO SECTION
    html.Section([
        html.Div([
            html.H1(["World-Class Results ", html.Br(), " Stellar Mentorship"]),
            html.P([
                "You don't really need \"help.\" You’re already smart, young, and hungry for success.", html.Br(),
                "All you need is a nudge from someone who’s walked the path", html.Br(),
                "and lived to tell the tale—unfiltered and unafraid."
            ]),
            html.A("See How", href="#Value", className="btn-hero")
        ], className="hero-content fade-in"),

        html.Div("Scroll Down ↓",
                 className="scroll-down",
                 id="scrollDownBtn"  # We'll attach JS to scroll into view
        )
    ], className="hero", id="home"),

    # ABOUT SECTION
    html.Section([
        html.H2("About Aryan D. Khedkar"),
        html.P(
            "I was born in a small Indian city where summers scorched, winters barely existed, "
            "and neighbors knew your business before you did. Growing up in a professor’s home meant "
            "the dinner table was always crowded with books and spirited debates.",
            className="section-intro"
        ),
        html.P(
            "Fast-forward through my teens (and countless late-night study sessions), I landed in the top 1% globally "
            "in the IB program, which paved the way to Imperial College London for Physics. "
            "Three months in, I met Sofia—my future wife—by handing her a copy of The Alchemist "
            "before she even knew my name.",
            className="section-intro"
        ),
        html.P(
            "The journey wasn’t all smooth. I left university just shy of final exams for a start-up dream, got stuck in visa limbo, "
            "and learned firsthand how resilience and faith can become your best friends. "
            "Today, I’m happily married at 21, growing a renewable energy start-up, "
            "and mentoring students to aim high—without losing their soul in the process.",
            className="section-intro"
        ),
        html.Div([
            html.P(
                "(Images are currently omitted for lean deployment. You can add them later.)",
                style={"color": "#aaa", "fontSize": "0.95rem"}
            ),
            html.P([
                "Check out my startup ",
                html.A("Candela Power",
                       href="https://candelapower.co.uk/",
                       target="_blank",
                       style={"color": "var(--accent)", "fontWeight": "600"}),
                ", where I mesh science, data, and business to tackle real-world energy challenges. "
                "Let’s work together to spark your own breakthrough—academic, personal, or otherwise."
            ], style={"maxWidth": "700px", "margin": "0 auto", "color": "#ccc"})
        ], className="About-content")
    ], id="About", className="fade-in"),

    # VALUE SECTION
    html.Section([
        html.H2("Value & Focus Areas"),
        html.P(
            "Empowering you to tackle life’s biggest transitions—without losing your sense of humor.",
            className="section-intro"
        ),
        html.Div([
            html.Div([
                html.H3("Academic Excellence"),
                html.P(
                    "From scoring in the top 1% globally to studying Physics at Imperial, I’ve tested "
                    "every 'study hack' in the book. I’ll help you cultivate smarter habits and get the grades you want."
                )
            ], className="Value-card"),

            html.Div([
                html.H3("Personal Growth"),
                html.P(
                    "Success is more than accolades. It’s about building grit, emotional well-being, and "
                    "a sense of purpose. I’ll share real-life tools (and maybe a dad joke or two) "
                    "to keep you grounded and growing."
                )
            ], className="Value-card"),

            html.Div([
                html.H3("Career Guidance"),
                html.P(
                    "Not sure which path to choose? I blend data-driven insights with a splash of "
                    "spiritual perspective to help you find—or create—a career that fuels you for the long run."
                )
            ], className="Value-card"),
        ], className="Value-grid")
    ], id="Value", className="fade-in"),

    # TESTIMONIALS SECTION
    html.Section([
        html.H2("Testimonials"),
        html.P(
            "Hear what clients say about their journey with Higher You.",
            className="section-intro"
        ),
        html.Div([
            html.Div([
                html.P(
                    "“I thought all coaching was just fluff until Aryan got me to rework my entire study routine. "
                    "Now I'm heading to my dream university and feeling more confident than ever!”",
                    className="testimonial-text"
                ),
                html.P("— A. Sharma", className="testimonial-author")
            ], className="testimonial-slide active", id="slide1"),

            html.Div([
                html.P(
                    "“Aryan’s mix of analytical thinking and heartfelt advice is like nothing I've seen. "
                    "It's part physics, part deep life talk—and it works.”",
                    className="testimonial-text"
                ),
                html.P("— L. Green", className="testimonial-author")
            ], className="testimonial-slide", id="slide2"),

            html.Div([
                html.P(
                    "“He helped me see I could do more than just get good grades—I could actually love "
                    "what I'm studying. Best decision I've made for my future.”",
                    className="testimonial-text"
                ),
                html.P("— M. Evans", className="testimonial-author")
            ], className="testimonial-slide", id="slide3"),

            html.Div([
                html.Button("1", id="btnSlide1", **{"data-slide-num": "1"}),
                html.Button("2", id="btnSlide2", **{"data-slide-num": "2"}),
                html.Button("3", id="btnSlide3", **{"data-slide-num": "3"}),
            ], className="testimonial-nav")
        ], className="testimonials")
    ], id="testimonials", className="fade-in"),

    # PRICING SECTION
    html.Section([
        html.H2("Pricing"),
        html.P(
            "Your investment in personal growth and transformational mentorship.",
            className="section-intro"
        ),
        html.Div([
            # Single Session
            html.Div([
                html.H3("Single Session"),
                html.Div("£100 / hour", className="price"),
                html.Ul([
                    html.Li("1 Hour of One-on-One Coaching"),
                    html.Li("Personalized Action Steps"),
                    html.Li("Immediate Growth Strategies"),
                ]),
                html.A("Book Now", href="#contact")
            ], className="pricing-plan"),

            # 5-Session Package
            html.Div([
                html.H3("5-Session Package"),
                html.Div("£450", className="price"),
                html.Ul([
                    html.Li("5 Hours of Coaching"),
                    html.Li("Progress Tracking & Feedback"),
                    html.Li("Ongoing Email Support"),
                    html.Li("Save £50 Overall"),
                ]),
                html.A("Book Now", href="#contact")
            ], className="pricing-plan"),

            # 10-Session Package
            html.Div([
                html.H3("10-Session Package"),
                html.Div("£850", className="price"),
                html.Ul([
                    html.Li("10 Hours of Coaching"),
                    html.Li("Deep-Dive Transformation"),
                    html.Li("High-Level Accountability"),
                    html.Li("Save £150 Overall"),
                ]),
                html.A("Book Now", href="#contact")
            ], className="pricing-plan"),
        ], className="pricing-grid")
    ], id="pricing", className="fade-in"),
    # BACK TO TOP BUTTON
    html.Button("↑", id="backToTop", **{"aria-label": "Back to top"})
])
