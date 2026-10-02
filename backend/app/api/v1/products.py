from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/products", tags=["products"])

# Datos en memoria solo para probar (Fase 4/6 lo pasa a PostgreSQL)
_FAKE_PRODUCTS = [
    {"id": 1, "name": "Laptop", "stock": 10},
    {"id": 2, "name": "Mouse", "stock": 50},
]


@router.get("")
def list_products():
    return _FAKE_PRODUCTS


@router.get("/{product_id}")
def get_product(product_id: int):
    for p in _FAKE_PRODUCTS:
        if p["id"] == product_id:
            return p
    raise HTTPException(status_code=404, detail="Producto no encontrado")


@router.post("")
def create_product(body: dict):
    new_id = max(p["id"] for p in _FAKE_PRODUCTS) + 1 if _FAKE_PRODUCTS else 1
    new_product = {"id": new_id, "name": body.get("name", "Sin nombre"), "stock": body.get("stock", 0)}
    _FAKE_PRODUCTS.append(new_product)
    return new_product
