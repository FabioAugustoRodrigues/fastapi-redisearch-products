from fastapi import APIRouter

from ..schemas.product_schema import ProductRequest
from ..services.product_service import ProductService

router = APIRouter()
product_service = ProductService()


@router.post("/")
async def create_product(product: ProductRequest):
    product_service.create_product(product.dict())

    return product