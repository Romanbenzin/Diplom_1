expected_receipt_after_remove = (
    "(==== Булочка с кунжутом ====)\n"
    "= sauce ketchunese =\n"
    "= filling beef =\n"
    "= filling carrot =\n"
    "= sauce ketchunese =\n"
    "(==== Булочка с кунжутом ====)\n"
    "\n"
    "Price: 28"
)

expected_receipt_before_remove = (
    "(==== Булочка с кунжутом ====)\n"
    "= sauce ketchunese =\n"
    "= filling beef =\n"
    "(==== Булочка с кунжутом ====)\n"
    "\n"
    "Price: 18"
)

expected_receipt_before_move_ingredient = (
    "(==== Булочка с кунжутом ====)\n"
    "= sauce ketchunese =\n"
    "= filling carrot =\n"
    "= sauce ketchunese =\n"
    "= filling beef =\n"
    "(==== Булочка с кунжутом ====)\n"
    "\n"
    "Price: 28"
)
