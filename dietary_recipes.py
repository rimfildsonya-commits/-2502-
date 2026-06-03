from ingredients import Ingredient
from recipes import Recipe
class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients):
        self.diet_type = diet_type
        super().__init__(title, ingredients)
    def scale(self, ratio:float):
        new_scale = super().scale(ratio)
        return DietaryRecipe(new_scale.title, self.diet_type, new_scale.ingredients)
    def __str__(self):
        return f"[{self.diet_type}]{self.title}: {self.ingredients}"