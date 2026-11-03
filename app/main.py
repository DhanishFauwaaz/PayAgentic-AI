from fastapi import FastAPI
from app.routers import procurement

app = FastAPI(
    title="PayAgentic-AI Backend",
    description="Autonomous B2B Procurement & Escrow Engine powered by Meta Llama 3 & PayPal REST APIs",
    version="1.0.0"
)

# Include the Procurement Router
app.include_router(procurement.router, prefix="/api/v1/procurement", tags=["Procurement & AI Auditing"])

@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "system": "PayAgentic-AI Active",
        "hackathon": "Meta Global AI & PayPal AI Hackathons"
    }