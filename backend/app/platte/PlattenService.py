from fastapi import HTTPException
from surrealdb import RecordID


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


async def UpdatePlatteService(platten_id, platte, db):
    try:
        # Prepare the data for database update
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
        
        # Update the specific platte by ID
        result = await db.update(f"platte:{platten_id}", platte_data)
        
        if not result:
            raise HTTPException(status_code=404, detail=f"Platte with ID {platten_id} not found")
        
        return {
            "status": "success",
            "result": result
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database operation failed: {str(e)}")


async def GetPlatteByIDService(platten_id, db):

    # print(platten_id)
    
    try:
        # Retrieve specific platte by ID from the database
        result = await db.select(RecordID('platte', platten_id))

        # print(result)
        
        if not result:
            raise HTTPException(status_code=404, detail=f"Platte with ID {platten_id} not found")
        
        return {
            "status": "success",
            "result": result
        }
    
    except HTTPException:
        raise
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

    
async def DeletePlatteByIDService(platten_id, db):
    try:
        # Delete specific platte by ID from the database
        result = await db.delete(f"platte:{platten_id}")
        
        if not result:
            raise HTTPException(status_code=404, detail=f"Platte with ID {platten_id} not found")
        
        return {
            "status": "success",
            "message": f"Platte with ID {platten_id} deleted successfully",
            "result": result
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database operation failed: {str(e)}")

    
