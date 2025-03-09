from fastapi import APIRouter, HTTPException
from app.core.cohere_client import co # call Cohere client

router = APIRouter()

@router.get("/generate")
async def generate_text(prompt: str):
    """
    Given Prompt Call Cohere Text Generate API
    """
    try:
        response = co.generate(
            prompt=prompt,
            max_tokens=50,
            temperature=0.3,
            stop_sequences=["--"]
        )
        # Extract the response text
        generated_text = response.generations[0].text.stript()
        return {"generated_text": generated_text}
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))