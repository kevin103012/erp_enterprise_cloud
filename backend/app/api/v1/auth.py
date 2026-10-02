from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/ping")
def ping():
    return {"module": "auth", "status": "ok"}


@router.post("/login")
def login_fake(body: dict):
    # Prueba sin BD ni JWT real (Fase 8 lo reemplaza)
    username = body.get("username", "demo")
    return {"token": "fake-jwt-para-pruebas", "username": username}
