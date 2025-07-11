from fastapi import APIRouter, HTTPException, Depends
from surrealdb import AsyncSurreal

from app.db.database import get_db

from app.platte.PlattenSchema import Platte


router = APIRouter(
    prefix="/platte",
    tags=["platte"],
)


@router.post("/")
async def create_platte(
        platte: Platte, 
        db: AsyncSurreal = Depends(get_db)
    ):
    try:
        result = await db.create(
            "platte", {
                "name": platte.name,
                "koerperteil": platte.koerperteil,
                "status": platte.status,
                "productzustand": platte.productzustand,
                "sdk": platte.sdk,
                "masse": platte.masse,
                "hersteller": platte.hersteller,
                "bewahrungsort": platte.bewahrungsort,
                "bestellungstag": platte.bestellungstag,
                "ansprechpartner": platte.ansprechpartner,
                "beschreibung": platte.beschreibung,
                "chartData": platte.chartData,
            }
        )

        return {
            "status": "success", 
            "result": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database operation failed: {str(e)}")