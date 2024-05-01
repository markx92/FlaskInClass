from pprint import pprint

from app.db import BaseModel

class Sandwich(BaseModel):

    SHEET_NAME = "sandwiches"

    COLUMNS = ["name", "description", "price", "url"]

    SEEDS = [
        {
            'name': 'Cheesesteak',
            'description': 'Take me to Philly!',
            'price': 11.99,
            'url': 'https://images.themodernproper.com/billowy-turkey/production/posts/2022/PhillyCheesesteaks_12.jpg?w=1200&q=82&auto=format&fit=crop&dm=1674669377&s=d55a675dabc0279efae35b9a9253bc97'
        },
        {
            'name': 'Meatball',
            'description': 'Ground beef and pork to satisfy your craving for ground beef and pork.',
            'price': 10.49,
            'url': 'https://d3s8tbcesxr4jm.cloudfront.net/recipe-images/v3/easy-meatball-sub/0_medium.jpg'
        },
        {
            'name': 'Italian Stallion',
            'description': 'It has all the answers.',
            'price': 9.99,
            'url': 'https://www.carolynscooking.com/wp-content/uploads/2020/05/New-Classic-Italian-Sub-13.jpg'
        },
        {
            'name': 'Caprese Love',
            'description': 'Some version of healthy.',
            'price': 8.99,
            'url': 'https://www.eatingwell.com/thmb/uAo_rveXpw6wB0j01eOstQoLS9A=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/caprese-sandwich-e0bb2b846cf14cd7a0eb2d3f4d4b6aa2.jpg'
        }
    ]




if __name__ == "__main__":

    print("------------")
    print("EXISTING RECORDS:")
    sandwiches = Sandwich.all()
    print("FOUND", len(sandwiches), "Sandwiches:")
    if any(sandwiches):
        for sandwich in sandwiches:
            #breakpoint()
            pprint(dict(Sandwich))
    else:
        #if input("Seed products? (Y/N)? ").upper() == "Y":
        #    print("SEEDING RECORDS...")
        #    Product.seed()
        print("SEEDING RECORDS...")
        Sandwich.seed()

    print("------------")
    print("FIND RECORD GIVEN ITS IDENTIFIER...")
    sandwich = Sandwich.find(1)
    print(sandwich.name)

    print("------------")
    print("FILTERING RECORDS...")
    matches = sandwich.where(name="Cheesesteak")
    print(len(matches))
    sandwich = matches[0]
    print(sandwich.name)

    print("------------")
    print("CREATING NEW PRODUCT...")
    params = {
        "name": "Bread only",
        "price":3.99,
        "description":"organic whole grain loaf!",
        "url": "https://sallysbakingaddiction.com/wp-content/uploads/2021/01/multigrain-bread-loaf-2.jpg"
    }
    Sandwich.create(params)
