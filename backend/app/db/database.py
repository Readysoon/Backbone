from dotenv import load_dotenv
from surrealdb import AsyncSurreal
import logging
import os
from contextlib import asynccontextmanager

# Load environment variables from the .env file
load_dotenv()

DATABASE_URL = os.getenv("SURREALDB_URL")
DATABASE_USER = os.getenv("SURREALDB_USER")
DATABASE_PASS = os.getenv("SURREALDB_PASS")
DATABASE_NAMESPACE = os.getenv("SURREALDB_NAMESPACE")
DATABASE_NAME = os.getenv("SURREALDB_DATABASE")

@asynccontextmanager
async def get_db():
    """
    Get database connection with proper cleanup
    """
    print(f"Attempting to connect to SurrealDB at {DATABASE_URL}")

    print(DATABASE_URL, DATABASE_USER, DATABASE_PASS, DATABASE_NAMESPACE, DATABASE_NAME)

    db = None
    try:
        print(f"Attempting to connect to {DATABASE_URL}")
        db = AsyncSurreal(DATABASE_URL)
        print("Created SurrealDB instance")
        
        await db.connect()
        print("Connected to SurrealDB")
        
        await db.signin({"username": DATABASE_USER, "password": DATABASE_PASS})
        print("Signed in to SurrealDB")
        
        await db.use(DATABASE_NAMESPACE, DATABASE_NAME)
        print(f"Using namespace '{DATABASE_NAMESPACE}' and database '{DATABASE_NAME}'")
        
        yield db
    except Exception as e:
        logging.error(f"Error connecting to SurrealDB: {e}")
        raise e
    finally:
        if db is not None:
            try:
                await db.close()
                print("Closed SurrealDB connection")
            except Exception as close_error:
                logging.error(f"Error closing SurrealDB connection: {close_error}")
