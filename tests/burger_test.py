from unittest.mock import Mock

from bun import Bun
from burger import Burger
from ingredient import Ingredient
from static_data.ingredient_name_price import INGREDIENT_PRICE_KETCHUNESE, INGREDIENT_NAME_KETCHUNESE, \
    INGREDIENT_PRICE_BEEF, INGREDIENT_NAME_BEEF, INGREDIENT_NAME_CARROT, INGREDIENT_PRICE_CARROT, BURGER_NAME_BUN, \
    BURGER_PRICE_BUN
from static_data.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from static_data.static_data_for_burger_tests import expected_receipt_after_remove, expected_receipt_before_remove, \
    expected_receipt_before_move_ingredient


class TestBurger:
    def setup_method(self):
        # Создание булочки
        self.new_bun = Bun(BURGER_NAME_BUN, BURGER_PRICE_BUN)
        # Мок объекта кетчунез
        ketchunese_mock = Mock()
        ketchunese_mock.get_name.return_value = INGREDIENT_NAME_KETCHUNESE
        ketchunese_mock.get_price.return_value = INGREDIENT_PRICE_KETCHUNESE

        # Мок объекта мясо
        beef_mock = Mock()
        beef_mock.get_name.return_value = INGREDIENT_NAME_BEEF
        beef_mock.get_price.return_value = INGREDIENT_PRICE_BEEF

        # Мок объекта морковь
        carrot_mock = Mock()
        carrot_mock.get_name.return_value = INGREDIENT_NAME_CARROT
        carrot_mock.get_price.return_value = INGREDIENT_PRICE_CARROT

        # Создание ингредиентов
        ketchunese = Ingredient(INGREDIENT_TYPE_SAUCE, ketchunese_mock.get_name.return_value, ketchunese_mock.get_price.return_value)
        beef = Ingredient(INGREDIENT_TYPE_FILLING, beef_mock.get_name.return_value, beef_mock.get_price.return_value)
        carrot = Ingredient(INGREDIENT_TYPE_FILLING, carrot_mock.get_name.return_value, carrot_mock.get_price.return_value )
        # Создание объекта бургер
        self.new_burger = Burger()
        # Добавление булочки бургеру
        self.new_burger.set_buns(self.new_bun)
        # Добавление ингредиентов
        self.new_burger.add_ingredient(ketchunese)
        self.new_burger.add_ingredient(beef)
        self.new_burger.add_ingredient(carrot)
        self.new_burger.add_ingredient(ketchunese)

    def test_add_ingredient(self):
        expected_price_before_remove = (BURGER_PRICE_BUN + 2) + (INGREDIENT_PRICE_KETCHUNESE * 2) + INGREDIENT_PRICE_CARROT + INGREDIENT_PRICE_BEEF
        assert self.new_burger.get_price() == expected_price_before_remove

    def test_remove_ingredient(self):
        self.new_burger.remove_ingredient(3)
        expected_price_after_remove = (BURGER_PRICE_BUN + 2) + INGREDIENT_PRICE_KETCHUNESE + INGREDIENT_PRICE_CARROT + INGREDIENT_PRICE_BEEF
        assert self.new_burger.get_price() == expected_price_after_remove

    def test_add_ingredient_and_receipt_burger(self):
        assert expected_receipt_after_remove == self.new_burger.get_receipt()

    def test_remove_ingredient_and_receipt_burger(self):
        self.new_burger.remove_ingredient(2)
        self.new_burger.remove_ingredient(2)
        assert expected_receipt_before_remove == self.new_burger.get_receipt()

    def test_move_ingredient_and_receipt_burger(self):
        self.new_burger.move_ingredient(1, 3)
        assert expected_receipt_before_move_ingredient == self.new_burger.get_receipt()
