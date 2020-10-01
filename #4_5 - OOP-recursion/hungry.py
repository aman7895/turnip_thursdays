from collections import defaultdict
from typing import List


class FridgeItem:
    def __init__(self, name, expiration_quantity):

        self.name = name
        self.cache = {}
        self.expiration_quantity = expiration_quantity

        self.cache[self.expiration_quantity[0]] = self.expiration_quantity[1]
        self.total_quantity = sum(self.cache.values())

        print(self.name, " : ", self.cache)

    def update_cache(self, expiration_quantity: List[str]):
        if expiration_quantity[0] not in self.cache:
            self.cache[expiration_quantity[0]] = 0

        self.cache[expiration_quantity[0]] += expiration_quantity[1]

        print(self.name, " : ", self.cache)

    def has_enough_availability(self, current_date, quantity):
        available_quantity = 0
        for date in self.cache.keys():
            if date >= current_date:
                available_quantity += self.cache[date]

        return available_quantity >= quantity

    def get_current_items(self, current_date):
        quantity = 0
        for date in self.cache.keys():
            if date >= current_date:
                quantity += self.cache[date]
        return quantity

    def view_items(self):
        print(self.cache)


class Fridge:
    def __init__(self):
        self.fridge = {}
        self.recipes = {}
        self.food_items = {}

    def add_items_to_fridge(self, food_item: str, item_quantity: str, expiry_time: int = 0):
        expiry_quantity = [expiry_time, item_quantity]

        if food_item not in self.food_items:
            fridge_item = FridgeItem(food_item, expiry_quantity)
            self.food_items[food_item] = fridge_item
        else:
            fridge_item = self.food_items[food_item]
            fridge_item.update_cache(expiry_quantity)

        print(self.food_items)

    def add_new_recipe(self, recipe_name: str, recipe_ingredients: dict):
        self.recipes[recipe_name] = recipe_ingredients
        print("Recipes: ", self.recipes)

    def get_ingredients(self, recipe_items: dict, date: int) -> dict:
        total_ingredients = {}
        for item, quantity in recipe_items:
            if item in self.recipes:
                for i, q in self.get_ingredients(self.recipes[item].items(), date).items():
                    if i not in total_ingredients:
                        total_ingredients[i] = 0
                    if item in self.food_items.keys():
                        total_ingredients[i] += q * (quantity - self.food_items[item].get_current_items(date))
                    else:
                        total_ingredients[i] += q * quantity
            else:
                if item not in total_ingredients:
                    total_ingredients[item] = 0
                total_ingredients[item] += quantity
        return total_ingredients

    def create_recipe(self, recipe_name: str, date: int) -> bool:
        if recipe_name not in self.recipes:
            return False
        ingredients = self.get_ingredients(self.recipes[recipe_name].items(), date)

        for food_item, quantity in ingredients.items():
            fridge_item = self.food_items[food_item]
            if not fridge_item.has_enough_availability(date, quantity):
                return False

        return True


if __name__ == '__main__':
    fridge = Fridge()
    fridge.add_items_to_fridge("Tomato", 2, 10)
    fridge.add_items_to_fridge("Tomato", 2, 5)
    fridge.add_items_to_fridge("Onion", 2, 10)
    fridge.add_new_recipe("paste", {"Tomato": 2, "Onion": 1})
    print(fridge.create_recipe("paste", 10))
    fridge.add_new_recipe("Pasta", {"paste": 5, "Onion": 1})
    print(fridge.create_recipe("Pasta", 3))
