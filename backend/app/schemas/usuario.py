from uuid import UUID
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class UsuarioCreate(BaseModel):
    username: str
    email: EmailStr
    nombres: str
    apellidos: str
    activo: bool = True


class UsuarioOut(BaseModel):
    id: UUID
    username: str
    email: str
    nombres: str
    apellidos: str
    activo: bool
    ultimo_acceso: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
