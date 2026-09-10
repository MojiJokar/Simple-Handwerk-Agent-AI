from pydantic import BaseModel
from typing import Optional


class Customer(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None


class CustomerRequest(BaseModel):
    customer: Customer
    problem: str
    location: Optional[str] = None
    urgency: str
    requested_date: Optional[str] = None


class AgentDecision(BaseModel):
    action: str
    reason: str
    response_text: str