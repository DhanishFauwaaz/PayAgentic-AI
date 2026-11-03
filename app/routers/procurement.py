from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agents.audit_agent import llama_agent

router = APIRouter()

class AuditRequest(BaseModel):
    contract_terms: str
    vendor_deliverable: str
    milestone_id: str

@router.post("/audit-milestone")
async def audit_milestone_endpoint(request: AuditRequest):
    """
    Receives B2B contract specifications and vendor deliverables, 
    then invokes Meta Llama 3 to audit compliance and return an escrow release decision.
    """
    if not request.contract_terms or not request.vendor_deliverable:
        raise HTTPException(status_code=400, detail="Contract terms and vendor deliverable cannot be empty.")

    # Call Meta Llama 3 Audit Agent
    audit_response = await llama_agent.audit_milestone(
        contract_terms=request.contract_terms,
        vendor_deliverable=request.vendor_deliverable
    )

    return {
        "milestone_id": request.milestone_id,
        "audit_status": "completed",
        "result": audit_response
    }