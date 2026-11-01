from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain import Order
from src.repository import OrderRow, SqlOrderRepository, make_engine


#Adicion de actividad crear un pedido de prueba 
def test_repository_commit():
    engine = make_engine()
    with Session(engine) as session:
        SqlOrderRepository(session).save(1, Order(120))
        SqlOrderRepository(session).save(2, Order(250))
        session.commit()
        assert session.scalar(select(OrderRow).where(OrderRow.id == 1)).total == 120
        row = session.scalar(select(OrderRow).where(OrderRow.id == 2))
        assert row.id == 2
        assert row.total == 250
        assert row.status == "NEW"

def test_repository_rollback():
    engine = make_engine()
    with Session(engine) as session:
        SqlOrderRepository(session).save(1, Order(120))
        SqlOrderRepository(session).save(2, Order(250))
        session.rollback()
        assert session.scalar(select(OrderRow).where(OrderRow.id == 1)) is None
        assert session.scalar(select(OrderRow).where(OrderRow.id == 2)) is None