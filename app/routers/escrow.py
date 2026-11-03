from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.paypal_service import paypal_client
from app.core.redis_lock import redis_manager

router = APIRouter()

class PayoutRequest(BaseModel):
    milestone_id: str
    vendor_email: str
    amount: str
    audit_approved: bool

@router.post("/release-funds")
async def release_funds_endpoint(request: PayoutRequest):
    """
    Triggers PayPal escrow payout if and only if the AI audit approved the milestone,
    protected by a Redis distributed lock to prevent duplicate payouts.
    """
    if not request.audit_approved:
        raise HTTPException(
            status_code=400, 
            detail="Escrow release denied: AI Audit milestone approval required."
        )

    lock_key = f"lock:milestone:{request.milestone_id}"
    
    # Attempt to acquire distributed lock
    is_locked = await redis_manager.acquire_lock(lock_key, expire_seconds=15)
    if not is_locked:
        raise HTTPException(
            status_code=409,
            detail="Conflict: Payout for this milestone is already being processed or has been locked."
        )

    try:
        # Execute PayPal Payout
        payout_response = await paypal_client.release_escrow_payout(
            payout_batch_id=f"BATCH_{request.milestone_id}",
            receiver_email=request.vendor_email,
            amount=request.amount
        )

        return {
            "status": "SUCCESS",
            "message": "Escrow funds successfully released to vendor via PayPal API with Redis concurrency protection.",
            "payout_details": payout_response
        }
    finally:
        # Release lock after execution
        await redis_manager.release_lock(lock_key)