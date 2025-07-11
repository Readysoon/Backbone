from fastapi import APIRouter, Depends
from surrealdb import AsyncSurreal
import logging

from app.db.database import get_db

from app.platte.PlattenSchema import Platte
from app.platte.PlattenService import CreatePlatteService, GetAllPlattenService


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

@router.get("/all")
async def get_all_plates(
        db: AsyncSurreal = Depends(get_db)
    ):
    return await GetAllPlattenService(
        db
    )


    