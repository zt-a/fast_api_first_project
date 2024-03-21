from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("Db cleared")
    await delete_tables()
    print("Db successfully")
    yield
    print("Exited[0]")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
