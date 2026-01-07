import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from datetime import datetime


# Load data
df = pd.read_csv("processed_sales.csv")
df["date"] = pd.to_datetime(df["date"])

# Create Dash app
app = Dash(__name__)

app.layout = html.Div(
    className="container",
    children=[
        html.Div(
            className="header",
            children=[
                html.H1("Pink Morsel Sales Visualiser"),
                html.P(
                    "Explore Pink Morsel sales over time by region. "
                    "The price increase occurred on 15 January 2021."
                ),
            ],
        ),

        html.Div(
            className="card",
            children=[
                html.Label("Select Region:"),
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
                ),
            ],
        ),

        html.Div(
            className="card",
            children=[
                dcc.Graph(id="sales-line-chart")
            ],
        ),
    ],
)

# Callback to update chart
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value"),
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    daily_sales = (
        filtered_df
        .groupby("date", as_index=False)["sales"]
        .sum()
        .sort_values("date")
    )

    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        labels={"date": "Date", "sales": "Total Sales ($)"},
        title=f"Pink Morsel Sales Over Time ({selected_region.capitalize()})"
    )

    # ✅ SAFE vertical line
   # Vertical line (NO annotation here)
    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="red",
    )

# Manual annotation (safe)
    fig.add_annotation(
        x="2021-01-15",
        y=daily_sales["sales"].max(),
        text="Price Increase",
        showarrow=True,
        arrowhead=2,
        ax=40,
        ay=-40,
        font=dict(color="red"),
    )


    fig.update_layout(
        plot_bgcolor="#0f172a",
        paper_bgcolor="#1e293b",
        font_color="#f8fafc",
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
