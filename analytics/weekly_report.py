import pandas as pd
from app.db import get_conn

conn = get_conn()

df = pd.read_sql("SELECT * FROM daily_metrics", conn)

print("weekly insights")

print("avg sleep:", df.sleep.mean())
print("avg mood:", df.mood.mean())

print("best day sleep:", df.loc[df.sleep.idxmax()])
