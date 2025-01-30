from fastapi import APIRouter
from ..schemas.product_schema import ProductRequest

router = APIRouter()



@router.post("/")
async def create_product(product: ProductRequest):
    return product