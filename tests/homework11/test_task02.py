from homework11.task02 import Order, elder_discount, morning_discount


def test_order_morning_discount():
    order = Order(100, morning_discount)
    assert order.final_price() == 75


def test_order_elder_discount():
    order = Order(100, elder_discount)
    assert order.final_price() == 10
