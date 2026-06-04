from ingredients import Ingredient
from recipes import Recipe
from dietary_recipes import DietaryRecipe
from shopping_list import ShoppingList
import pytest
def create():
    ing1 = Ingredient("QQQ", 67, "мг")
    assert ing1.name == "QQQ"
    assert ing1.quantity == 67.0
    assert ing1.unit == "мг"
def test_str():
    ing1 = Ingredient("ААЙ", 67, "г")
    x = "ААЙ: 67.0 г"
    assert str(ing1) == x
def test_eq_1():
    ing1 = Ingredient("ХРРР", 67, "г")
    ing2 = Ingredient("ХРРР", 52, "г")
    assert ing1 == ing2
def test_eq2():
    ing1 = Ingredient("CCC", 67, "г")
    ing2 = Ingredient("XXX", 67, "г")
    assert ing1!= ing2
def test_eq3():
    ing1 = Ingredient("ЗЗЗ", 67, "кг")
    ing2 = Ingredient("ЗЗЗ", 67, "г")
    assert ing1!=ing2
def test_creat():
    ingred1 = [Ingredient("ZZ", 56, "г"), Ingredient("SS", 444, "кг")]
    recipe1 = Recipe("Burmalda", ingred1)
    assert recipe1.title == "Burmalda"
    assert recipe1.ingredients[0].name == "ZZ"
    assert recipe1.ingredients[0].quantity == 56
    assert recipe1.ingredients[0].unit == "г"
    assert recipe1.ingredients[1].name == "SS"
    assert recipe1.ingredients[1].quantity == 444
    assert recipe1.ingredients[1].unit == "кг"
def test_add1():
    recipe1 = Recipe("Mellstroy", [Ingredient("ZZ", 56, "г")])
    recipe1.add_ingredient(Ingredient("ЧЧ", 76, "кг"))
    assert recipe1.ingredients[1].name == "ЧЧ"
def test_add2():
    recipe1 = Recipe("Salat", [Ingredient("CCCC", 52, "г")])
    recipe1.add_ingredient(Ingredient("CCCC", 67, "г"))
    assert recipe1.ingredients[0].quantity == 119
def test_scale1():
    recipe1 = Recipe("ZZZ", [Ingredient("OOO", 67, "г")])
    recipe2 = recipe1.scale(8)
    assert recipe1.ingredients[0].quantity == 67
    assert recipe2.ingredients[0].quantity == 536
def test_scale2():
    recipe1 = Recipe("AAA", [Ingredient("m", 888, "мг")])
    multiply = recipe1.scale(7)
    assert multiply.ingredients[0].quantity == 6216
def test_scale3():
    recipe1 = Recipe("X", [Ingredient("brmld", 111, "г")])
    with pytest.raises(ValueError):
        recipe1.scale(-2)
def test_len():
    recipe1 = Recipe("Mellstroy", [Ingredient("A", 777, "кг"), Ingredient("B", 1488, "мг"), Ingredient("C", 228, "г"), Ingredient("d", 67, "кг")])
    assert len(recipe1) == 4
def test_addrec1():
    recipe1 = Recipe("AAA", [Ingredient("m", 888, "мг")])
    list1 = ShoppingList()
    list1.add(recipe1, 1)
    assert list1.items[0][0].quantity == 888
def test_addrec2():
    recipe1 = Recipe("BBB", [Ingredient("xzzz", 677, "г")])
    list1 = ShoppingList()
    with pytest.raises(ValueError):
        list1.add_recipe(recipe1, -4)
def test_removerec1():
    list1 = ShoppingList()
    list1.add_recipe(Recipe("x", [Ingredient("salat", 1488, "г")]), 1)
    list1.add_recipe(Recipe("y", [Ingredient("tort", 52, "кг")]), 1)    
    list1.add_recipe(Recipe("z", [Ingredient("xcvvv", 67, "кг")]), 2)
    list1.remove_recipe("x")
    assert list1.items[0][1] == "y"
def test_removerec2():
    list1 = ShoppingList()
    list1.add_recipe(Recipe("x", [Ingredient("x", 1488, "г")]), 1)
    list1.add_recipe(Recipe("z", [Ingredient("y", 67, "кг")]), 1)
    list1.remove_recipe("vv") 
    assert len(list1.items) == 2
def test_getlist1():
    list1 = ShoppingList()
    list1.add_recipe(Recipe("BBB", [Ingredient("xzzz", 677, "г")]),1)
    list1.add_recipe(Recipe("XXX", [Ingredient("xzzz", 100, "г")]), 1)
    list2 = list1.get_list()
    assert list2[0].quantity == 777
    assert len(list2)==1
def test_getlist2():
    list1 = ShoppingList()
    list1.add_recipe(Recipe("tort", [Ingredient("morkovka", 1488, "кг"), Ingredient("listok", 18, "кг"), Ingredient("chh", 777, "г")]), 1 )
    list2 = list1.get_list()
    assert list2[0].name == "morkovka"
    assert list2[1].name == "listok"
    assert list2[2].name == "chh"
def test_add():
    list1 = ShoppingList()
    list1.add_recipe(Recipe("A", [Ingredient("C", 67, "мг")]), 1)   
    list2 = ShoppingList()
    list2.add_recipe(Recipe("B", [Ingredient("D", 76, "кг")]), 1)
    newlist = list1 + list2
    assert len(newlist.items) == 2
    assert len(list1.items) == 1
    assert len(list2.items) == 1