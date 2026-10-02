import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

# URL del POOLER (puerto 6543, modo transaction), NO la directa 5432.
# Ejemplo en Supabase Dashboard > Connect > Transaction Pooler:
# postgresql://postgres.USUARIO:PASSWORD@aws-0-region.pooler.supabase.com:6543/postgres
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:CHANGE_ME@localhost:5432/postgres",
)

# Pool chico: Supabase Free = 60 directas / 200 pooler.
# Con 4 devs + API, si cada uno abre 20 se cae. Por eso 5 + 10.
engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_pre_ping=True,
    pool_recycle=300,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Dependency para FastAPI: abre 1 sesion por request y la cierra."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
