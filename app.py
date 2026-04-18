from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px


dataformat = pd.read_csv("formatted.csv")


dataformat["date"] = pd.to_datetime(dataformat["date"])
dataformat = dataformat.sort_values("date")


app = Dash(__name__)


app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f8",
        "minHeight": "100vh",
        "padding": "30px",
        "fontFamily": "Arial, sans-serif"
    },
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            id="app-header",
            style={
                "textAlign": "center",
                "color": "#222",
                "marginBottom": "30px"
            }
        ),

        html.Div(
            style={
                "width": "80%",
                "margin": "0 auto",
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.1)"
            },
            children=[
                html.H3(
                    "Filter by Region",
                    style={
                        "marginBottom": "10px",
                        "color": "#444",
                        "textAlign": "center"
                    }
                ),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={
                        "marginBottom": "20px",
                        "textAlign": "center"
                    },
                    labelStyle={
                        "marginRight": "20px",
                        "fontSize": "16px"
                    }
                ),

                dcc.Graph(id="sales-chart")
            ]
        )
    ]
)

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered = dataformat
    else:
        filtered = dataformat[dataformat["region"].str.lower() == selected_region]

    daily_sales = filtered.groupby("date", as_index=False)["sales"].sum()

    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales Over Time - {selected_region.title()}",
        labels={"date": "Date", "sales": "Sales"}
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        title_x=0.5
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)