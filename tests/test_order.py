
import pytest

from src.domain import CustomerHasDebt, Order


def test_vip_discount():
    o = Order(100, vip=True)
    assert o.confirm() == 85
    assert o.status == "CONFIRMED"

#Nueva prueba 1 
def test_vip_discount_200():
    x = Order(200, vip=True)
    assert x.confirm() == 170
    assert x.status == "CONFIRMED"

def test_regular_no_discount():
    assert Order(100).confirm() == 100

#Nueva prueba 2
def test_regular_no_discount_200():
    assert Order(200).confirm() == 200

def test_customer_debt():
    with pytest.raises(CustomerHasDebt):
        Order(100).confirm(customer_debt=50)

# Adicion de RED
def test_cannot_confirm_twice(): 
    order = Order(100) 
    order.confirm() 
    with pytest.raises(ValueError, match="already confirmed"): 
        order.confirm() 

@pytest.mark.parametrize("total", [0, -1])
def test_invalid_total(total):
    with pytest.raises(ValueError):
        Order(total).confirm()
