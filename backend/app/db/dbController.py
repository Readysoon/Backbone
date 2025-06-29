from fastapi import APIRouter, HTTPException, Depends
from surrealdb import Surreal
from app.db.database import get_db

router = APIRouter(
    prefix="/db",
    tags=["db"],
)

@router.get("/test")
async def test_db_connection(
        db: Surreal = Depends(get_db)
    ):
    try:
        # A simple query to test connection
        result = await db.query("RETURN true;")
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")