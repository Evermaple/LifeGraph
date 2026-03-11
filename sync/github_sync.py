import requests
import os
from datetime import date
from app.db import get_conn

TOKEN = os.getenv("GITHUB_TOKEN")
USER = os.getenv("GITHUB_USER")


def sync():

    url = f"https://api.github.com/users/{USER}/events"

    headers = {"Authorization": f"token {TOKEN}"}

    r = requests.get(url, headers=headers).json()

    commits = 0

    for e in r:
        if e["type"] == "PushEvent":
            commits += len(e["payload"]["commits"])

    today = date.today().isoformat()

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
    UPDATE daily_metrics
    SET deepwork=?
    WHERE date=?
    """, (commits, today))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    sync()
