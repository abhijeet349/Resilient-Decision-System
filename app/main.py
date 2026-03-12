from fastapi import FastAPI
from pydantic import BaseModel

from app.database import cursor
from app.workflow_engine import process_workflow

app = FastAPI()

class RequestData(BaseModel):

    request_id: str
    income: int
    credit_score: int


@app.get("/")
def home():
    return {"message": "Workflow Decision System Running"}


@app.post("/process")
def process(data: RequestData):

    cursor.execute(
        "SELECT result FROM workflow_state WHERE request_id=?",
        (data.request_id,)
    )

    existing = cursor.fetchone()

    if existing:

        return {
            "request_id": data.request_id,
            "decision": existing[0],
            "note": "duplicate request"
        }

    input_data = {
        "income": data.income,
        "credit_score": data.credit_score
    }

    decision, rules = process_workflow(data.request_id, input_data)

    return {
        "request_id": data.request_id,
        "decision": decision,
        "rules_triggered": rules
    }
