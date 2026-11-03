# PayAgentic-AI

Autonomous B2B Procurement & Escrow Engine powered by Meta Llama 3, FastAPI, Redis, and PayPal REST APIs.

## Overview

PayAgentic-AI bridges contract compliance and financial settlements by pairing an AI auditing agent with automated payment execution. When vendors submit milestone deliverables, Meta Llama 3 evaluates the output against contractual requirements. Once verified, the platform safely releases escrow funds via PayPal, protected by Redis distributed locking to prevent duplicate transactions.

## Features

- **AI Milestone Auditing:** Uses Meta Llama 3 to evaluate contract compliance and return structured approval verdicts.
- **Automated Payouts:** Executes PayPal Sandbox payouts automatically upon positive audit validation.
- **Concurrency Protection:** Employs Redis distributed locks (`redis-py`) to safeguard payout routes against race conditions and double-spending.
- **OpenAPI Documentation:** Auto-generated interactive documentation via FastAPI Swagger UI.

## Tech Stack

- **Framework:** FastAPI (Python 3.11+)
- **AI Model:** Meta Llama 3 API
- **Payments:** PayPal REST APIs (Sandbox)
- **Concurrency / Caching:** Redis
- **Validation:** Pydantic / Pydantic-Settings

## Getting Started

### 1. Local Setup

```bash
# Clone repository
git clone [https://github.com/your-username/PayAgentic-AI.git](https://github.com/your-username/PayAgentic-AI.git)
cd PayAgentic-AI

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
