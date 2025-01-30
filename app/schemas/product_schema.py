from pydantic import BaseModel

class ProductRequest(BaseModel):
    description: str
    supplier: str