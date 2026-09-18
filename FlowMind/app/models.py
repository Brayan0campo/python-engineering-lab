from pydantic import BaseModel, Field

class ProcessRequest(BaseModel):
    supplier: str
    invoice_number: str
    amount: float = Field(gt=0)
    currency: str
    description: str

class ProcessingResult(BaseModel):
    invoice_number: str
    approval_status: str