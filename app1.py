import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load the cleaned data
df = pd.read_csv("cleaned_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Group by date to aggregate total sales per day
daily_sales = df.groupby("date")["sales"].sum().reset_index()

# Create line chart using Plotly Express
fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Daily Pink Morsel Sales",
    labels={"date": "Date", "sales": "Sales ($)"},
)

# Add a vertical line on Jan 15, 2021 (price increase date)
fig.add_vline(x="2021-01-15", line_dash="dash", line_color="red")
fig.update_layout(
    title_x=0.5,
    annotations=[
        dict(
            x="2021-01-15",
            y=max(daily_sales["sales"]),
            xref="x",
            yref="y",
            text="Price Increase",
            showarrow=True,
            arrowhead=1,
            ax=0,
            ay=-40,
        )
    ]
)

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

# Run app
if __name__ == '__main__':
    app.run(debug=True)

