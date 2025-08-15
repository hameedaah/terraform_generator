from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from typing import Dict, Any
from app.generator.prompt_builder import build_prompt
from app.generator.llm_handler import generate_script_with_gemini


class TerraformRequest(BaseModel):
    provider: str
    region: str
    resource_type: str
    resource_name: str
    attributes: Dict[str, Any]

app = FastAPI(
    title="Terraform Generator API",
    description="An API to generate Terraform scripts using the Gemini API",
    version="1.0.0"
)

@app.post("/generate", response_class=PlainTextResponse)
async def generate(request: TerraformRequest):
    try:
        prompt = build_prompt(
            provider=request.provider,
            region=request.region,
            resource_type=request.resource_type,
            resource_name=request.resource_name,
            attributes=request.attributes
        )
        script = generate_script_with_gemini(prompt)
        return script
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
