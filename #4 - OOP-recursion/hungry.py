class Fridge:
    def __init__(self):
        self.fridge = {}
        self.recipes = {}

    def add_items_to_fridge(self, food_item: str, item_quantity: str) -> dict:
        if food_item not in self.fridge:
            self.fridge[food_item] = 0
        self.fridge[food_item] += item_quantity
        print(self.fridge)
        return self.fridge

    def add_new_recipe(self, recipe_name: str, recipe_ingredients: dict):
        self.recipes[recipe_name] = recipe_ingredients
        print(self.recipes)

    def get_ingredients(self, recipe_name) -> dict:
        total_ingredients = {}

        for item, quantity in self.recipes[recipe_name].items():
            if item in self.recipes.keys():
                temp = self.get_ingredients(item)
                for i, q in temp.items():
                    if i not in total_ingredients:
                        total_ingredients[i] = 0
                    total_ingredients[i] += q * (quantity - self.fridge[item])
            else:
                if item not in total_ingredients:
                    total_ingredients[item] = 0
                total_ingredients[item] += quantity
        print(total_ingredients)
        return total_ingredients

    def can_create_with_recipe(self, recipe_name: str) -> bool:
        if recipe_name not in self.recipes:
            return False
        ingredients = self.get_ingredients(recipe_name)
        for item, quantity in ingredients.items():
            if quantity > self.fridge[item]:
                return False
        return True


if __name__ == '__main__':
    fridge = Fridge()
    fridge.add_items_to_fridge("Tomato", 2)
    fridge.add_items_to_fridge("Onion", 2)
    fridge.add_items_to_fridge("paste", 1)
    fridge.add_new_recipe("paste", {"Tomato": 2, "Onion": 1})
    print(fridge.can_create_with_recipe("paste"))
    fridge.add_new_recipe("Pasta", {"paste": 1, "Onion": 1})
    print(fridge.can_create_with_recipe("Pasta"))