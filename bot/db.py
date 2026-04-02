import aiosqlite
import os

DB_PATH = os.getenv("DB_PATH")
DB_SCHEMA_PATH = os.getenv("DB_SCHEMA_PATH")

def get_db():
    return aiosqlite.connect(DB_PATH)

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        with open(DB_SCHEMA_PATH) as f:
            await db.executescript(f.read())
        await db.commit()
