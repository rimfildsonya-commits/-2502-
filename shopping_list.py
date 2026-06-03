from ingredients import Ingredient
from recipes import Recipe
from dietary_recipes import DietaryRecipe
class ShoppingList:
    def __init__(self, items):
        self.items = items
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions<=0:
            raise ValueError(
                "Количество порций должно быть положительным"
            )
        rec = recipe.scale(portions)
        for ingredient in rec.ingredients:
            self.items.append((ingredient, recipe.title))
    def remove_recipe(self, title:str):
        new = []
        for x in self.item:
            if x[1]!=title:
                new.append(x)
        self.item = new
    def get_list(self):
        res = {}
        for x in self.items:
            ingredient = x[0]
            b = (ingredient.name, ingredient.unit)
            if b in res:
                res[b]+= ingredient.quantity
            else:
                res[b] = ingredient.quantity
        res2 = []
        for b, c in res.items:
            res2.append(Ingredient(b[0], c, b[1]))
        res2.sort(key=lambda x: x.name)
        return res2
    def __add__(self, ther:ShoppingList):
        return (self.item + other.item)