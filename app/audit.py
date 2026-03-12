from app.database import cursor, conn

def write_audit(request_id, rule_name, decision):

    cursor.execute(
        "INSERT INTO audit_log(request_id, rule_name, decision) VALUES(?,?,?)",
        (request_id, rule_name, decision)
    )

    conn.commit()
