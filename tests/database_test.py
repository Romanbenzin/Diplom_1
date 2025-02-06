from database import Database

class TestDatabase:
    def test_database_buns(self):
        new_base = Database()
        assert len(new_base.buns) == 3

    def test_database_ingredients(self):
        new_base = Database()
        assert len(new_base.ingredients) == 6
