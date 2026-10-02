from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.usuario import UsuarioOut
from app.repositories import usuario_repository as repo

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/count")
def count_users(db: Session = Depends(get_db)):
    return {"total": repo.count_usuarios(db)}


@router.get("", response_model=list[UsuarioOut])
def list_users(limit: int = 100, offset: int = 0, db: Session = Depends(get_db)):
    return repo.list_usuarios(db, limit=limit, offset=offset)


@router.get("/{user_id}", response_model=UsuarioOut)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = repo.get_usuario_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user
