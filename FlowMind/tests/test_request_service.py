from app.models import ProcessRequest
from app.services.request_service import determine_approval_status

def test_auto_approval_for_low_amount():
    request = ProcessRequest(
        supplier="ACME S.A.S.",
        invoice_number="INV-001",
        amount=500_000,
        currency="COP",
        description="Office supplies",
    )

    result = determine_approval_status(request)
    assert result == "AUTO_APPROVAL"


def test_auto_approval_for_medium_amount():
    request = ProcessRequest(
        supplier="ACME S.A.S.",
        invoice_number="INV-002",
        amount=3_000_000,
        currency="COP",
        description="Software licensing",
    )

    result = determine_approval_status(request)
    assert result == "STANDARD_APPROVAL"


def test_auto_approval_for_high_amount():
    request = ProcessRequest(
        supplier="ACME S.A.S.",
        invoice_number="INV-003",
        amount=8_500_000,
        currency="COP",
        description="Software services",
    )

    result = determine_approval_status(request)
    assert result == "MANAGER_APPROVAL"