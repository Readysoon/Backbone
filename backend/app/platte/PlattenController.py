from re import M
from fastapi import APIRouter, Depends
from surrealdb import AsyncSurreal
import logging

from app.db.database import get_db

from app.platte.PlattenSchema import Platte
from app.platte.PlattenService import CreatePlatteService, UpdatePlatteService, GetAllPlattenService


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

@router.get("/all")
async def get_all_platten(
        db: AsyncSurreal = Depends(get_db)
    ):
    return await GetAllPlattenService(
        db
    )


    