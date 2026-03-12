import sqlite3

conn = sqlite3.connect("workflow.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS workflow_state(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id TEXT UNIQUE,
    status TEXT,
    result TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS audit_log(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id TEXT,
    rule_name TEXT,
    decision TEXT
)
""")

conn.commit()
