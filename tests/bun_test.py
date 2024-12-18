from bun import Bun

class TestBun:

    def test_name(self):
        new_bun = Bun('Булочка с маком', 12)

        assert new_bun.get_name() == 'Булочка с маком'

    def test_price(self):
        new_bun = Bun('Булочка с маком', 12)

        assert new_bun.get_price() == 12