from fastapi import FastAPI
from app.models import ProcessRequest
from app.services.request_service import determine_approval_status

app = FastAPI(
    title="FlowMind",
    description="Intelligent Process Automation Platform",
    version="0.1.0",
)

@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "FlowMind API is running",
        "status": "ok",
    }

@app.post("/requests")
def create_request(request: ProcessRequest) -> dict[str, str]:
    approval_status = determine_approval_status(request)

    return {
        "invoice_number": request.invoice_number,
        "approval_status": approval_status,
    }