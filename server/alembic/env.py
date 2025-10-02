# alembic/env.py
from __future__ import annotations

import asyncio
import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import create_async_engine

# --- make your project importable when running "alembic" from repo root ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# --- app imports (absolute) ---
from core.config import settings
from core.database import Base
from models import tables  # noqa: F401  (ensure models are registered)

# --- Alembic Config & logging ---
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --- metadata for autogenerate ---
target_metadata = Base.metadata

# --- DB URL handling: async for runtime, sync for Alembic config/offline ---
ASYNC_DB_URL = settings.database_url


def make_sync_url(url: str) -> str:
    if url.startswith("postgresql+asyncpg"):
        return url.replace("postgresql+asyncpg", "postgresql+psycopg")
    if url.startswith("sqlite+aiosqlite"):
        return url.replace("sqlite+aiosqlite", "sqlite")
    if url.startswith("mysql+aiomysql"):
        return url.replace("mysql+aiomysql", "mysql+pymysql")
    return url


SYNC_DB_URL = make_sync_url(ASYNC_DB_URL)
# set on the Alembic config so "alembic current" etc. have a URL
config.set_main_option("sqlalchemy.url", SYNC_DB_URL)

IS_SQLITE = SYNC_DB_URL.startswith("sqlite")


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode (no DB connection)."""
    context.configure(
        url=SYNC_DB_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_as_batch=IS_SQLITE,  # helpful for SQLite schema changes
    )
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    """Configure context and run migrations with a given (sync) connection."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,        # detect type changes
        render_as_batch=IS_SQLITE,
    )
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode using an async engine."""
    connectable = create_async_engine(ASYNC_DB_URL, poolclass=pool.NullPool)
    async with connectable.connect() as async_conn:
        await async_conn.run_sync(do_run_migrations)
    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
