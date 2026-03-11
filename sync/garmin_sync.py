# crontab -e
# 0 7 * * * python sync/garmin_sync.py

from garminconnect import Garmin
from datetime import date
from app.db import get_conn
import os

EMAIL = os.getenv("GARMIN_EMAIL")
PASSWORD = os.getenv("GARMIN_PASSWORD")


def sync():

    client = Garmin(EMAIL, PASSWORD)
    client.login()

    today = date.today().isoformat()

    steps = client.get_steps_data(today)[0]["steps"]
    sleep = client.get_sleep_data(today)["dailySleepDTO"]["sleepTimeSeconds"]/3600

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
    INSERT OR REPLACE INTO daily_metrics(date,steps,sleep)
    VALUES(?,?,?)
    """, (today, steps, sleep))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    sync()
