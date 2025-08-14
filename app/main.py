from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from typing import List
from typing import Dict, Any

# Define your request model
class Resource(BaseModel):
    type: str
    instance_type: str
    count: int = 1

class TerraformRequest(BaseModel):
    resource_type: str
    attributes: Dict[str, Any]

# Create FastAPI app
app = FastAPI(
    title="Terraform Generator API",
    description="An API to generate Terraform scripts using the Gemini API",
    version="1.0.0"
)

    
# FastAPI Endpoint
@app.post("/generate", response_class=PlainTextResponse)
async def generate(request: TerraformRequest):
    """
    Endpoint to receive a structured JSON request and return a Terraform script.   
    """
    try:
        # Pass the validated data directly to the generation function
        terraform_script = generate_terraform_script(request.resource_type, request.attributes)
        return terraform_script
    except Exception as e:
        # A more general error handler in case something goes wrong
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An internal server error occurred.")

