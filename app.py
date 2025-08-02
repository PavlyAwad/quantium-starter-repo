import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load and prepare data
df = pd.read_csv("cleaned_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Pink Morsel Sales Dashboard"

regions = ["north", "east", "south", "west"]

# App layout with CSS classes
app.layout = html.Div(className="main-container", children=[
    html.H1("Pink Morsel Sales Visualiser"),

    html.Div(className="radio-container", children=[
        html.Label("Select Region:"),
        dcc.RadioItems(
            id="region-selector",
            options=[{"label": r.capitalize(), "value": r} for r in regions] + [{"label": "All", "value": "all"}],
            value="all",
            inline=True
        )
    ]),

    dcc.Graph(id="sales-line-chart")
])

# Callback to update graph
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df.copy()
    else:
        filtered_df = df[df["region"] == selected_region]

    daily_sales = filtered_df.groupby("date")["sales"].sum().reset_index()

    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales - {selected_region.capitalize() if selected_region != 'all' else 'All Regions'}",
        labels={"date": "Date", "sales": "Sales ($)"}
    )

    fig.add_vline(x="2021-01-15", line_dash="dash", line_color="red")
    fig.update_layout(
        title_x=0.5,
        annotations=[
            dict(
                x="2021-01-15",
                y=max(daily_sales["sales"]) if not daily_sales.empty else 0,
                xref="x", yref="y",
                text="Price Increase",
                showarrow=True, arrowhead=1,
                ax=0, ay=-40,
            )
        ]
    )

    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)
