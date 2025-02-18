from ..services.product_service import ProductService

import csv
import redis

def import_csv_to_redisearch(csv_filename: str):
    product_service = ProductService()
    
    with open(csv_filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        
        for idx, row in enumerate(reader):
            description, supplier = row
            product = {"description": description, "supplier": supplier}
            product_service.create_product(product)

    print("CSV data successfully imported into RediSearch!")

if __name__ == "__main__":
    import_csv_to_redisearch("/srv/output/fake_products.csv")