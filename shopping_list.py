from ingredients import Ingredient
from recipes import Recipe
from dietary_recipes import DietaryRecipe
class ShoppingList:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        rec = recipe.scale(portions)
        for ingredient in rec.ingredients:
            self.items.append((ingredient, recipe.title))
    def remove_recipe(self, title: str):
        new = []
        for x in self.items:
            if x[1] != title:
                new.append(x)
        self.items = new
    def get_list(self):
        res = {}
        for x in self.items:
            ingredient = x[0]
            key = (ingredient.name, ingredient.unit)
            if key in res:
                res[key] += ingredient.quantity
            else:
                res[key] = ingredient.quantity
        result = []
        for key, quantity in res.items():
            result.append(Ingredient(key[0], quantity, key[1]))
        result.sort(key=lambda x: x.name)
        return result
    def __add__(self, other):
        new_list = ShoppingList()
        new_list.items = self.items.copy() + other.items.copy()
        return new_list