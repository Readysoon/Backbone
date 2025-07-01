from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from surrealdb import Surreal, RecordID
import logging

from app.db.dbController import router as db_router
from app.db.database import get_db

app = FastAPI()

# Configure CORS to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(db_router)

@app.get("/")
async def read_root():
	return {"Hello": "World!"}

@app.get("/create-grocery")
async def create_grocery_record():
    """
    Create a grocery record using SurrealDB
    """
    try:
        async with get_db() as db:
            # Create a record
            result = await db.create(RecordID("grocery", "1"), {
                "name": "Banana",
                "quantity": 10,
            })
            return {"status": "success", "result": result}
    except Exception as e:
        logging.error(f"Error creating grocery record: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to create grocery record: {str(e)}")
