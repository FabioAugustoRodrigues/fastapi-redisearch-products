from fastapi import APIRouter

from ..schemas.product_schema import ProductRequest
from ..services.product_service import ProductService

router = APIRouter()
product_service = ProductService()


@router.post("/")
async def create_product(product: ProductRequest):
    product_service.create_product(product.dict())

    return product

@router.get("/")
async def search_products(description: str):
    return product_service.search_product_by_description(description)