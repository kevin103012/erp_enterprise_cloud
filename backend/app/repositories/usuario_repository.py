from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.usuario import Usuario


def count_usuarios(db: Session) -> int:
    """SELECT COUNT(*) FROM usuarios — 1 sola conexion del pool, se cierra en get_db."""
    return db.query(func.count(Usuario.id)).scalar() or 0


def list_usuarios(db: Session, limit: int = 100, offset: int = 0):
    return (
        db.query(Usuario)
        .order_by(Usuario.created_at.desc())
        .offset(offset)
        .limit(min(limit, 100))
        .all()
    )


def get_usuario_by_id(db: Session, user_id: str):
    return db.query(Usuario).filter(Usuario.id == user_id).first()
