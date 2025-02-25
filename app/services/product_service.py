from ..indexes.products import create_products_index
from ..connection import create_redis_connection

from redisearch import Query, Client

import random

class ProductService:
    def __init__(self):
        self.redis_connection = create_redis_connection()
        self.product_index = create_products_index(self.redis_connection)

    def create_product(self, id: int, product: dict):
        return self.product_index.redis.hset(self.generate_key(id), mapping=product)

    def search_product_by_description(self, description: str):
        query_string = f'@description:({description}*)'
        query = Query(query_string).verbatim()
        return self.product_index.search(query)

    def generate_key(self, id):
        return "products:" + str(id)