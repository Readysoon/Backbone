from fastapi import APIRouter, HTTPException
from app.db.database import get_db

router = APIRouter(
    prefix="/db",
    tags=["db"],
)

@router.get("/test")
async def test_db_connection():
    try:
        async with get_db() as db:
            # A simple query to test connection
            result = await db.query("RETURN true;")
            return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")