from ingredients import Ingredient
from recipes import Recipe
class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients
    def add_ingredient(self, ingredient: Ingredient):
        for x in self.ingredients:
            if x.name == ingredient.name and x.unit == ingredient.unit:
                x.quantity+=ingredient.quantity
                return
        self.ingredients.append(ingredient)    
    @staticmethod
    def is_valid_ratio(ratio):
        if type(ratio) == int or type(ratio) == float:
            if ratio>0:
                return True
            else:
                return False
    def scale(self, ratio: float):
        ingred = []
        for x in self.ingredients:
            cop = Ingredient(x.name, x.quantity * ratio, x.unit)
            ingred.append(cop)
        return(self.title, ingred)
    def __len__(self):
        return len(self.ingredients)+1
    def __str__(self):
        res = self.title + ': '
        for x in self.ingredients:
            res  = res + ' ' + x.name + '(' + str(x.quantity)+ x.unit+'.'+','
        return res[:-1]