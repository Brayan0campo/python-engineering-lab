from pydantic import BaseModel

class ProcessRequest(BaseModel):
    supplier: str
    invoice_number: str
    amount: float
    currency: str
    description: str