import csv
import random
from faker import Faker

def generate_fake_products(filename: str, num_products: int = 100000):
    fake = Faker()
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Description", "Supplier"])
        
        for _ in range(num_products):
            description = fake.sentence(nb_words=random.randint(2, 6))
            supplier = fake.company()
            writer.writerow([description, supplier])

if __name__ == "__main__":
    generate_fake_products("/srv/output/fake_products.csv", num_products=100000)
    print("CSV file with fake products generated successfully!")
