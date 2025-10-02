from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.database import engine, Base
from api.routes.openai_router import router as openai_router
from api.routes.gemini_router import router as gemini_router

app = FastAPI()

# Dev convenience: create tables. In prod, use Alembic and remove this.
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(openai_router)
app.include_router(gemini_router)