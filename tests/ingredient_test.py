from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest

class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", [(INGREDIENT_TYPE_SAUCE, 'ketchunese', 999999), (INGREDIENT_TYPE_FILLING, 'carrot', 2)])
    def test_ingredient_name(self, ingredient_type, name, price):
        new_ingredient = Ingredient(ingredient_type, name, price)

        assert  new_ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", [(INGREDIENT_TYPE_SAUCE, 'ketchunese', 999999), (INGREDIENT_TYPE_FILLING, 'carrot', 2)])
    def test_ingredient_price(self, ingredient_type, name, price):
        new_ingredient = Ingredient(ingredient_type, name, price)

        assert  new_ingredient.get_price() == price

    @pytest.mark.parametrize("ingredient_type, name, price", [(INGREDIENT_TYPE_SAUCE, 'ketchunese', 999999), (INGREDIENT_TYPE_FILLING, 'carrot', 2)])
    def test_ingredient_type(self, ingredient_type, name, price):
        new_ingredient = Ingredient(ingredient_type, name, price)

        assert  new_ingredient.get_type() == ingredient_type