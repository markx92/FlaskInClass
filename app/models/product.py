from pprint import pprint

from app.db import BaseModel

class Product(BaseModel):

    SHEET_NAME = "products"

    COLUMNS = ["name", "description", "price", "url"]

    SEEDS = [
        {
            'name': 'Strawberries',
            'description': 'Juicy organic strawberries.',
            'price': 4.99,
            'url': 'https://picsum.photos/id/1080/360/200'
        },
        {
            'name': 'Cup of Tea',
            'description': 'An individually-prepared tea or coffee of choice.',
            'price': 3.49,
            'url': 'https://picsum.photos/id/225/360/200'
        },
        {
            'name': 'Textbook',
            'description': 'It has all the answers.',
            'price': 129.99,
            'url': 'https://picsum.photos/id/24/360/200'
        }
    ]




if __name__ == "__main__":

    print("------------")
    print("EXISTING RECORDS:")
    products = Product.all()
    print("FOUND", len(products), "PRODUCTS:")
    if any(products):
        for product in products:
            #breakpoint()
            pprint(dict(product))
    else:
        #if input("Seed products? (Y/N)? ").upper() == "Y":
        #    print("SEEDING RECORDS...")
        #    Product.seed()
        print("SEEDING RECORDS...")
        Product.seed()

    print("------------")
    print("FIND RECORD GIVEN ITS IDENTIFIER...")
    product = Product.find(1)
    print(product.name)

    print("------------")
    print("FILTERING RECORDS...")
    matches = Product.where(name="Strawberries")
    print(len(matches))
    product = matches[0]
    print(product.name)

    Product.create(params)
