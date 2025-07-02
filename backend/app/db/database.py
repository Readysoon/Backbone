from surrealdb import Surreal, AsyncSurreal
from fastapi import HTTPException
import os
from contextlib import asynccontextmanager

DATABASE_URL = os.getenv("SURREALDB_URL")
DATABASE_USER = os.getenv("SURREALDB_USER")
DATABASE_PASS = os.getenv("SURREALDB_PASS")
DATABASE_NAMESPACE = os.getenv("SURREALDB_NAMESPACE")
DATABASE_NAME = os.getenv("SURREALDB_DATABASE")

async def get_db():
    """Database dependency that provides a connected and authenticated SurrealDB instance"""
    db = None
    try:
        print("This is the updated db connection 3")
        print(DATABASE_URL, DATABASE_USER, DATABASE_PASS, DATABASE_NAMESPACE, DATABASE_NAME)
        try:
            db = AsyncSurreal(DATABASE_URL)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"db = AsyncSurreal: {str(e)}")
        
        try:
            # Connect to the database
            await db.connect()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"await db.connect(): {str(e)}")
        
        try:
            # Select namespace and database
            await db.use(DATABASE_NAMESPACE, DATABASE_NAME)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"namespace and database: {str(e)}")

        try:
            # Sign in to the database
            await db.signin({
                "username": DATABASE_USER,
                "password": DATABASE_PASS
            })
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"signin: {str(e)}")

        yield db
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")
    finally:
        # Always close the connection when the dependency is done
        if db:
            try:
                await db.close()
            except Exception as e:
                print(f"Warning: Error closing database connection: {str(e)}")