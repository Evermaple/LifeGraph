from fastapi import FastAPI
import pandas as pd
from .db import get_conn

app = FastAPI()


@app.get("/metrics")
def metrics():

    conn = get_conn()

    df = pd.read_sql("SELECT * FROM daily_metrics", conn)

    conn.close()

    return df.to_dict(orient="records")


@app.get("/stats")
def stats():

    conn = get_conn()

    df = pd.read_sql("SELECT * FROM daily_metrics", conn)

    conn.close()

    return {
        "avg_sleep": float(df.sleep.mean()),
        "avg_steps": float(df.steps.mean()),
        "avg_mood": float(df.mood.mean())
    }
