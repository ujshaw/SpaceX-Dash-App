import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import requests
import json

from dash.dependencies import Input, Output
from plotly import graph_objs as go


app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Layout of Dash App
app.layout = html.Div(
    children=[
        html.Div(
            id="wrapper",
            className="visible",
            children=[
                html.Div(
                    id="header",
                    className="section",
                    children=[
                        html.Div(
                            className="header-inner",
                            children=[
                                html.Div(
                                    id="navigation",
                                    children=[
                                        html.Ul(
                                            className="nav-links",
                                            children=[
                                                html.Li(className="nav-item",children=[html.A("Launches",href="www.spacex.com/vehicles/falcon-9")]),
                                                html.Li(className="nav-item",children=[html.A("Launchpads",href="www.spacex.com/vehicles/falcon-9")]),
                                                html.Li(className="nav-item",children=[html.A("Landpads",href="www.spacex.com/vehicles/falcon-9")]),
                                                html.Li(className="nav-item",children=[html.A("Dragons",href="www.spacex.com/vehicles/falcon-9")]),
                                                html.Li(className="nav-item",children=[html.A("Rockets",href="www.spacex.com/vehicles/falcon-9")]),
                                                html.Li(className="nav-item",children=[html.A("Starlink",href="www.spacex.com/vehicles/falcon-9")]),
                                                html.Li(className="nav-item",children=[html.A("Ships",href="www.spacex.com/vehicles/falcon-9")]),
                                                html.Li(className="nav-item",children=[html.A("Capsules",href="www.spacex.com/vehicles/falcon-9")]),
                                                html.Li(className="nav-item",children=[html.A("Cores",href="www.spacex.com/vehicles/falcon-9")]),
                                                html.Li(className="nav-item",children=[html.A("Payloads",href="www.spacex.com/vehicles/falcon-9")]),
                                                html.Li(className="nav-item",children=[html.A("Crew",href="www.spacex.com/vehicles/falcon-9")]),
                                                html.Li(className="nav-item",children=[html.A("Roadster",href="www.spacex.com/vehicles/falcon-9")]),
                                                html.Li(className="nav-item",children=[html.A("SpaceX",href="www.spacex.com/vehicles/falcon-9")])
                                            ]
                                        )
                                    ]
                                ),
                                html.A(
                                    id="logo",
                                    href="/",
                                    children=[
                                        html.Img(src="/assets/images/logo.png")
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            id="menu-close",
                            style={'visibility':'hidden','opacity':'0'}
                            ),
                        html.Div(
                            id="menu",
                            style={'width':'0px'},
                            children=[
                                html.Div(
                                    id="menu-background",
                                    style={'transform':'matrix(1, 0, 0, 1, 0, 0)'},
                                ),
                            ]
                        ),
                    ]
                ),
                html.Div(
                    id="scroller",
                    children=[
                        html.Div(
                            id="feature",
                            className="section",
                            children=[
                                html.Div(
                                    id="parallax",
                                    className="background background-video-cover",
                                    style= {'transform':'translate3d(0px, 0px, 0px) scale3d(1, 1, 1) rotate3d(0, 0, 0.75, 0deg)','background-image':'url("https://www.spacex.com/static/images/backgrounds/starlink10.jpg")','visibility':'inherit','opacity':'1'}
                                ),
                                html.Div(
                                    className="section-inner feature",
                                    style={'height':'790px'},
                                    children=[
                                        html.Div(
                                            className="inner-left-bottom"
                                        ),
                                        html.Div(
                                            id="scrollme"
                                        )
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            className="section",
                            children=[
                                html.Div(
                                    className="background",
                                    style={'background-image':'url("https://www.spacex.com/static/images/backgrounds/starlink10.jpg")'}
                                ),
                                html.Div(
                                    className="section-inner resize",
                                    style={'height':'790px'}
                                )
                            ]
                        ),
                        html.Div(
                            className="section",
                            children=[
                                html.Div(
                                    className="background",
                                    style={'background-image':'url("https://www.spacex.com/static/images/backgrounds/starlink10.jpg")'}
                                ),
                                html.Div(
                                    className="section-inner resize",
                                    style={'height':'790px'}
                                )
                            ]
                        ),
                        html.Div(
                            className="section",
                            children=[
                                html.Div(
                                    className="background",
                                    style={'background-image':'url("https://www.spacex.com/static/images/backgrounds/starshipliftoff_desktop1.jpg")'}
                                ),
                                html.Div(
                                    className="section-inner resize",
                                    style={'height':'790px'}
                                )
                            ]
                        ),
                        html.Div(
                            className="section",
                            children=[
                                html.Div(
                                    className="background",
                                    style={'background-image':'url("https://www.spacex.com/static/images/backgrounds/home_demo2.jpg")'}
                                ),
                                html.Div(
                                    className="section-inner resize",
                                    style={'height':'790px'}
                                )
                            ]
                        ),
                        html.Div(
                            className="section collapse",
                            children=[
                                html.Div(
                                    className="background",
                                    style={'background-image':'url("https://www.spacex.com/static/images/backgrounds/home_moon.jpg")'}
                                ),
                                html.Div(
                                    className="section-inner resize",
                                    style={'height':'790px'}
                                )
                            ]
                        ),
                        html.Div(
                            id="footer",
                            className="section",
                            children=[
                                html.P(
                                    children=[
                                        html.Span('Data from '),
                                        html.A('SpaceX API',href="//github.com/r-spacex/SpaceX-API")
                                    ]
                                )
                            ]
                        )
                    ]
                )

            ],
        ),
        html.Div(
            id="modal",
            className="modal",
            children=[
                html.Div(
                    className="modal-bg"
                ),
                html.Div(
                    className="modal-inner"
                ),
                html.A(
                    className="modal-close"
                )
            ]
        )
    ]
)



if __name__ == "__main__":
    app.run_server(debug=True)
