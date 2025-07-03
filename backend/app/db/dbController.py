from fastapi import APIRouter, HTTPException, Depends
from surrealdb import AsyncSurreal

from app.db.database import get_db

from app.db.dbSchema import CreatePerson


router = APIRouter(
    prefix="/db",
    tags=["db"],
)


@router.post("/person")
async def test_person(
        person: CreatePerson, 
        db: AsyncSurreal = Depends(get_db)
    ):
    try:
        result = await db.create(
            "person", {
                "patient_name": person.patient_name,
                "date_of_birth": person.date_of_birth,
                "gender": person.gender,
                "contact_number": person.contact_number,
                "address": person.address,
            }
        )

        return {
            "status": "success", 
            "result": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database operation failed: {str(e)}")

