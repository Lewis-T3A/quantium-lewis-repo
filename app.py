from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

dataformat = pd.read_csv("formatted.csv")

dataformat["date"] = pd.to_datetime(df["date"])
dataformat = dataformat.sort_values("date")


daily_sales = dataformat.groupby("date", as_index=False)["sales"].sum()


fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Sales"}
)


app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)