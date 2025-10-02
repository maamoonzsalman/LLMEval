from __future__ import annotations
from datetime import datetime
from sqlalchemy import Text, String, ForeignKey, DateTime, func, UniqueConstraint, Index, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base

class SystemPrompt(Base):
    __tablename__ = "system_prompts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)   
    body: Mapped[str] = mapped_column(Text, nullable=False)           
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(),
                                                 onupdate=func.now(), nullable=False)

    test_prompts: Mapped[list["TestPrompt"]] = relationship(
        back_populates="system_prompt", cascade="all, delete-orphan"
    )

class TestPrompt(Base):
    __tablename__ = "test_prompts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    system_prompt_id: Mapped[int] = mapped_column(
        ForeignKey("system_prompts.id", ondelete="CASCADE"), nullable=False
    )
    body: Mapped[str] = mapped_column(Text, nullable=False)          
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    system_prompt: Mapped[SystemPrompt] = relationship(back_populates="test_prompts")

    __table_args__ = (
        UniqueConstraint("system_prompt_id", "body", name="uq_test_prompt_per_system"),
        Index("ix_test_prompts_system_prompt_id", "system_prompt_id"),
    )
