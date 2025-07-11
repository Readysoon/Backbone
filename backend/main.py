from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from surrealdb import Surreal, RecordID
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from app.platte.PlattenController import router as platten_router
# from app.db.database import get_db

app = FastAPI()

# Configure CORS to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(platten_router)

@app.get("/")
async def read_root():
	return {"Hello": "World!"}

