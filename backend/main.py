from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import httpx
import os

from app.db.dbController import router as db_router


app = FastAPI(
    title="Backbone API",
    description="Backend API for the Backbone project",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:4173"],  # Svelte dev and preview ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(db_router)


@app.get("/")
async def read_root():
	return {"Hello": "World!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)