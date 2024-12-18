from bun import Bun
from burger import Burger
from ingredient import Ingredient
from static_data.ingredient_name_price import INGREDIENT_PRICE_KETCHUNESE, INGREDIENT_NAME_KETCHUNESE, \
    INGREDIENT_PRICE_BEEF, INGREDIENT_NAME_BEEF, INGREDIENT_NAME_CARROT, INGREDIENT_PRICE_CARROT, BURGER_NAME_BUN, \
    BURGER_PRICE_BUN
from static_data.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_price_burger(self):
        # Создание булочки
        new_bun = Bun(BURGER_NAME_BUN, BURGER_PRICE_BUN)
        # Создание ингредиентов
        ketchunese = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME_KETCHUNESE, INGREDIENT_PRICE_KETCHUNESE)
        beef = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_NAME_BEEF, INGREDIENT_PRICE_BEEF)
        carrot = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_NAME_CARROT, INGREDIENT_PRICE_CARROT)
        # Создание объекта бургер
        new_burger = Burger()
        # Добавление булочки бургеру
        new_burger.set_buns(new_bun)
        # Добавление ингредиентов
        new_burger.add_ingredient(ketchunese)
        new_burger.add_ingredient(beef)
        new_burger.add_ingredient(carrot)
        new_burger.add_ingredient(ketchunese)

        expected_price_before_remove = (BURGER_PRICE_BUN + 2) + (INGREDIENT_PRICE_KETCHUNESE * 2) + INGREDIENT_PRICE_CARROT + INGREDIENT_PRICE_BEEF

        assert new_burger.get_price() == expected_price_before_remove

        new_burger.remove_ingredient(3)

        expected_price_after_remove = (BURGER_PRICE_BUN + 2) + INGREDIENT_PRICE_KETCHUNESE + INGREDIENT_PRICE_CARROT + INGREDIENT_PRICE_BEEF

        assert new_burger.get_price() == expected_price_after_remove
