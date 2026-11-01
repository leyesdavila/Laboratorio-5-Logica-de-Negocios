from datetime import UTC, datetime, timedelta

from src.security import can_cancel


def test_owner_within_24h():
    now = datetime.now(UTC)
    assert can_cancel("NEW", 1, 1, False, now - timedelta(hours=1), now)

def test_stranger_denied():
    now = datetime.now(UTC)
    assert not can_cancel("NEW", 1, 2, False, now, now)

def test_shipped_denied_even_admin():
    now = datetime.now(UTC)
    assert not can_cancel("SHIPPED", 1, 1, True, now, now)

def test_expired_denied():
    now = datetime.now(UTC)
    assert not can_cancel("NEW", 1, 1, False, now - timedelta(hours=25), now)
#Agregacion para actividad 6
#can_cancel(status, owner_id, user_id, is_admin, created_at, now=None)
#Caso en el que un administrador cancela pedido NEW de otro propietario 

def test_admin_can_cancel_new_order_of_other_owner():
    now = datetime.now(UTC)
    assert can_cancel("NEW", 2, 1, True, now, now)

#Cancelar justo 24hrs
def test_user_cancel_at_24hrs():
    now = datetime.now(UTC)
    assert not can_cancel("NEW", 1, 1, False, now - timedelta(hours=24), now)