import sqlite3

DB = "data/life.db"

def get_conn():
    return sqlite3.connect(DB)


def init_db():

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS daily_metrics(
        date TEXT PRIMARY KEY,
        sleep REAL,
        steps INTEGER,
        resting_hr INTEGER,
        mood INTEGER,
        deepwork REAL
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
