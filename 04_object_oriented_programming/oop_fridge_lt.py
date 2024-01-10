class Product:
    def __init__(self, name:str, quantity:float, **kwargs) -> None:
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = 'unit' # options: kg, g, L, ml
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}"
    
    def __repr__(self) -> str:
        return f"({self.name}, {self.quantity})"


class Recipe:
    ingredients = []
    instructions = []

    def __str__(self):
        return f"{self.ingredients}"

    def add_ingredient(self, product:Product):
        self.ingredients.append(product)

    def change_ingredient_quantity(self, ingredient_id:int, new_quantity:float):
        self.ingredients[ingredient_id].quantity = new_quantity

    def remove_ingredient(self, ingredient_id:int):
        self.ingredients.pop(ingredient_id)


class Fridge:
    contents = []

    def check_product(self, product_name:str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name == product_name:    
                """product.name.upper() == product_name.upper()"""
                """or product.name.lower() == product_name.lower()"""
                return product_id, product
        return None, None
    
    def check_product_quantity(self, product:Product, quantity:float):
        return product.quantity - quantity

    def add_product(self, name:str, quantity:float):
        product_id, product = self.check_product(name) # nenaudojamus kintamuosius galima vadinti tiesiog _
        if product is not None:
            product.quantity += quantity
        else:
            self.contents.append(Product(name, quantity))

    def remove_product(self, name:str, quantity:float):
        product_id, product = self.check_product(name)
        if product == None or (product.quantity - quantity < 0):
            return False
        elif product.quantity - quantity == 0:
            self.contents.pop(product_id)
        else:
            product.quantity -= quantity
        return True

    def print_contents(self):
        for product in self.contents:
            print(f"{product}")

    def check_recipe(self, recipe:Recipe):
        missing_product = []
        for ingredient in recipe.ingredients:
            product_id, product_fridge = self.check_product(ingredient.name)
            if  product_fridge is not None:
                missing_quantity = product_fridge.quantity - ingredient.quantity
                if missing_quantity < 0:
                    missing_product.append(Product(ingredient.name, abs(missing_quantity)))
            else:
                missing_product.append(ingredient)
        if len(missing_product) == 0:
            print("Dinner come!")
        else:
            print(f"Lost products : {missing_product}")


def select(number_of_choices):
    choice = ""
    while not choice.isnumeric():
        choice = input("    Jusu noras? : ")
        if choice.isnumeric():
            choice = int(choice)
            if choice == 0:
                print("Viso gero!")
                exit()
            elif choice <= number_of_choices:
                return (choice)
        print("Neteisingas noras, pabandyk dar karta")
        choice = ""


fridge = Fridge()
dinner = Recipe()

while True:
    print()
    print("^=..=^  Šaldytuvas  ^=..=^")
    print("  1: Pridėti produktą")
    print("  2: Išimti produktą")
    print("  3: Patikrinti kiekį šaldytuve")
    print("  4: Išspausdinti šaldytuvo turinį")
    print("  5: Sukurti receptą")
    print("  6: Išimti produktą is receptą")
    print("  7: Produktu kekį pakeisti receptoju")
    print("  8: Perziureti receptą")
    print("  9: Patikrinti receptą")
    print("  0: Išeiti")
    choice = select(9)
    if choice == 1:
        fridge.add_product(input("Name of product: "), float(input("Product quantity: ")))
    elif choice == 2:
        if fridge.remove_product(input("Name of product: "), 
                                 float(input("Product quantity: "))):
            print("Removed")
        else:
            print("Wrong product name or qauntity")
    elif choice == 3:
        product_id, product = fridge.check_product(input("Name of product: "))
        if product is not None:
            print(product.quantity)
        else:
            print(f"Fridge don't have that")   
    elif choice == 4:
        print(f"\n  === Fridge have : ===")
        fridge.print_contents()
    elif choice == 5:
        how_many_product = int(input("How many products in recipe? : "))
        for how in range(how_many_product):
            dinner.add_ingredient(Product(input("Name of product: "), 
                                 float(input("Product quantity: "))))
    elif choice == 6:
        dinner.remove_ingredient(int(input("Koki išimti? : "))-1)
    elif choice == 7:
        dinner.change_ingredient_quantity(int(input("Koki keisti? : "))-1, 
                                          float(input("Nauja kieki :")))
    elif choice == 8:
        print(dinner)
    elif choice == 9:
        fridge.check_recipe(dinner)
