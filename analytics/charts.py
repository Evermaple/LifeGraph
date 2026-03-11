import pandas as pd
import plotly.express as px
from app.db import get_conn


def generate():

    conn = get_conn()
    df = pd.read_sql("SELECT * FROM daily_metrics", conn)

    fig = px.line(df, x="date", y="sleep")
    fig.write_html("charts_sleep.html")

    fig2 = px.line(df, x="date", y="steps")
    fig2.write_html("charts_steps.html")

    fig3 = px.scatter(df, x="sleep", y="mood")
    fig3.write_html("sleep_mood.html")

if __name__ == "__main__":
    generate()
