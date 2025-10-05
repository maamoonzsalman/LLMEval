from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from api.routes.openai_router import router as openai_router
from api.routes.gemini_router import router as gemini_router
from api.routes.claude_router import router as claude_router
from api.routes.experiment_router import router as experiment_router
from api.routes.system_prompt_router import router as system_prompt_router
from api.routes.test_prompt_router import router as test_prompt_router

# Dev convenience: create tables. In prod, use Alembic and remove this.
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

app.include_router(openai_router)
app.include_router(gemini_router)
app.include_router(claude_router)
app.include_router(experiment_router)
app.include_router(system_prompt_router)
app.include_router(test_prompt_router)