from re import M
from fastapi import APIRouter, Depends
from surrealdb import AsyncSurreal
import logging

from app.db.database import get_db

from app.platte.PlattenSchema import Platte
from app.platte.PlattenService import CreatePlatteService, UpdatePlatteService, GetAllPlattenService, GetPlatteByIDService, DeletePlatteByIDService


router = APIRouter(
    prefix="/platte",
    tags=["platte"],
)


@router.post("/")
async def create_platte(
        platte: Platte, 
        db: AsyncSurreal = Depends(get_db)
    ):
    return await CreatePlatteService(
            platte,
            db
        )


# update like this

# {
#   "name": "Updated Platte Name",
#   "koerperteil": null,
#   "status": null,
#   "productzustand": null,
#   "sdk": null,
#   "masse": null,
#   "hersteller": null,
#   "bewahrungsort": null,
#   "bestellungstag": null,
#   "ansprechpartner": null,
#   "beschreibung": null,
#   "chartData": null
# }

@router.patch("/{platten_id}")
async def update_platte(
        platten_id: str,
        platte: Platte,
        db: AsyncSurreal = Depends(get_db)
    ):
    return await UpdatePlatteService(
            platten_id,
            platte,
            db
        )


@router.get("/")
async def get_all_platten(
        db: AsyncSurreal = Depends(get_db)
    ):
    return await GetAllPlattenService(
            db
        )

@router.get("/{platten_id}")
async def get_platte(
        platten_id: str,
        db: AsyncSurreal = Depends(get_db)
    ):
    return await GetPlatteByIDService(
            platten_id,
            db
        )


@router.delete("/{platten_id}")
async def delete_platte(
        platten_id: str,
        db: AsyncSurreal = Depends(get_db)
    ):
    return await DeletePlatteByIDService(
            platten_id,
            db
        )





    