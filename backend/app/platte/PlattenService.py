from fastapi import HTTPException


async def CreatePlatteService(platte, db):
    try:        
        # Prepare the data for database insertion
        platte_data = {
            "name": platte.name,
            "koerperteil": platte.koerperteil,
            "status": platte.status,
            "productzustand": platte.productzustand,
            "sdk": platte.sdk,
            "masse": platte.masse,
            "hersteller": platte.hersteller,
            "bewahrungsort": platte.bewahrungsort,
            "bestellungstag": platte.bestellungstag.isoformat() if platte.bestellungstag else None,
            "ansprechpartner": platte.ansprechpartner,
            "beschreibung": platte.beschreibung,
            "chartData": platte.chartData,
        }
                
        result = await db.create("platte", platte_data)
        
        return {
            "status": "success", 
            "result": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database operation failed: {str(e)}")


async def GetAllPlattenService(db):
    try:
        # Retrieve all platten from the database
        result = await db.select("platte")
        
        return {
            "status": "success",
            "result": result
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database operation failed: {str(e)}")
    
