import pandas as pd 
from dash import Dash,dcc,html
import plotly.express as px 



df=pd.read_csv("processed_sales.csv")

df["date"]=pd.to_datetime(df["date"])

df=df.sort_values("date")

daily_sales=df.groupby("date",as_index=False)["sales"].sum()

fig=px.line(
  daily_sales,
  x="date",
  y="sales",
  title="Pink Morsel Sales Over Time",
  labels={
    "date":"Date",
    "sales":"Total Sales ($)"
  }
)


app=Dash(__name__)

app.layout=html.Div(
  children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            style={"textAlign": "center"}
        ),

        html.P(
            "This chart shows total Pink Morsel sales over time. "
            "The price increase occurred on 15 January 2021.",
            style={"textAlign": "center"}
        ),

        dcc.Graph(figure=fig)
    ]
)


if __name__== "__main__":
  app.run(debug=True)
  
  














