from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ERP EnterpriseCloud API v1")

app.add_middleware(
    CORSMiddleware,  
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"service": "ERP EnterpriseCloud API", "version": "1.0 adete"}


# Routers por conectar cuando se creen (Fase 6):
# from app.api.v1 import auth, users, customers, products, sales, purchases, inventory
# app.include_router(auth.router, prefix="/api/v1")
