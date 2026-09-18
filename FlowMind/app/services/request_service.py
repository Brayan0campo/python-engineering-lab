from app.models import ProcessRequest

def determine_approval_status(request: ProcessRequest) -> str:
    if request.amount <= 1_000_000:
        return "AUTO_APPROVAL"

    if request.amount <= 5_000_000:
        return "STANDARD_APPROVAL"

    return "MANAGER_APPROVAL"