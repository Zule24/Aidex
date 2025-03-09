from fastapi import FastAPI
from app.routes import generate # Endpoint using Cohere

# FastAPI application
app = FastAPI(
    title="AIDEX Health API",
    description="Backend using FastAPI and Cohere API",
    version="1.0.0"
)

#  Adding endpoint to /api route
app.include_router(generate.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    # Run server (auto start when code changes)
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)