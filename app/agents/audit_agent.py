import httpx
from app.core.config import settings

class MetaLlamaAuditAgent:
    def __init__(self):
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.api_key = settings.MODEL_API_KEY

    async def audit_milestone(self, contract_terms: str, vendor_deliverable: str) -> dict:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "openai/gpt-oss-20b",
            "messages": [
                {
                    "role": "user",
                    "content": f"You are PayAgentic's autonomous B2B procurement auditor. Analyze the contract terms against the vendor deliverable and return a strict JSON response with keys: 'status' (APPROVED or REJECTED), 'confidence_score' (float), and 'reasoning' (string).\n\nContract Terms:\n{contract_terms}\n\nVendor Deliverable:\n{vendor_deliverable}"
                }
            ],
            "temperature": 0.1
        }

        async with httpx.AsyncClient(timeout=30.0) as client:
            try:
                response = await client.post(self.api_url, json=payload, headers=headers)
                response.raise_for_status()
                result = response.json()
                
                return {
                    "audit_result": result.get("choices", [{}])[0].get("message", {}).get("content", "No response"),
                    "provider": "Groq GPT-OSS"
                }
            except Exception as e:
                return {
                    "error": str(e),
                    "status": "FALLBACK_REVIEW",
                    "reasoning": "Meta API call failed, routed to manual escrow review."
                }

llama_agent = MetaLlamaAuditAgent()