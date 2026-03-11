import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("data/life.db")
cur = conn.cursor()

today = datetime.today()

for i in range(30):

    d = today - timedelta(days=i)

    sleep = round(random.uniform(6, 8), 1)
    steps = random.randint(4000, 12000)
    mood = random.randint(2, 5)
    deepwork = random.randint(1, 5)

    cur.execute("""
    INSERT OR REPLACE INTO daily_metrics
    (date,sleep,steps,mood,deepwork)
    VALUES (?,?,?,?,?)
    """, (d.date(), sleep, steps, mood, deepwork))

conn.commit()
conn.close()

print("demo data generated")
