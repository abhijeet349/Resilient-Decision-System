import random
import time

from app.rule_engine import RuleEngine
from app.database import cursor, conn
from app.audit import write_audit

engine = RuleEngine()

def external_service():

    # simulate failure

    if random.random() < 0.3:
        raise Exception("external service failure")

    return "ok"

def retry_external():

    retries = 3

    for i in range(retries):

        try:
            return external_service()

        except Exception:

            time.sleep(1)

    return "failed"

def process_workflow(request_id, data):

    service = retry_external()

    if service == "failed":
        return "external_failure", []

    decision, rules = engine.evaluate(data)

    cursor.execute(
        "INSERT INTO workflow_state(request_id,status,result) VALUES(?,?,?)",
        (request_id, "completed", decision)
    )

    conn.commit()

    for r in rules:
        write_audit(request_id, r, decision)

    return decision, rules
