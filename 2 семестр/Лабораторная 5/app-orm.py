from sqlalchemy import create_engine, Column, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func
from datetime import datetime

engine = create_engine("sqlite:///:memory:", echo=True)

Base = declarative_base()

class CurrencyRates(Base):
    __tablename__ = 'currency_rates'

    id = Column(String(3), primary_key=True)
    datetime = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    value = Column(Float)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # CREATE
    with Session() as session:
        usd = CurrencyRates(id='USD', value=90.9)
        gbp = CurrencyRates(id='GBP', value=100.9)
        eur = CurrencyRates(id='EUR', value=91)
        session.add_all([usd, gbp, eur])
        session.commit()

    input("Добавлены валюты. Проверка")

    # READ
    with Session() as session:
        stmt = select(CurrencyRates).where(
            CurrencyRates.value.between(90, 91)
        )
        for row in session.execute(stmt).scalars():
            print(f"ID: {row.id}, Datetime: {row.datetime}, Value: {row.value}")

    input("Обновление валюты. Проверка")

    # UPDATE
    with Session() as session:
        usd_to_update = session.query(CurrencyRates).filter_by(id='USD').first()
        if usd_to_update:
            usd_to_update.value = 100.9  # Обновляем значение
            session.commit()
            print("USD updated")
        else:
            print("USD not found")
        # READ - чтобы убедиться, что обновление прошло
        stmt = select(CurrencyRates)
        for row in session.execute(stmt).scalars(): # Получаем объекты, а не строки
            print(f"ID: {row.id}, Datetime: {row.datetime}, Value: {row.value}")

    # DELETE
    with Session() as session:
        # Получаем объект для удаления
        eur_to_delete = session.query(CurrencyRates).filter_by(id='EUR').first() #Исправлено: поиск по ID
        if eur_to_delete:
            session.delete(eur_to_delete) # удаляем объект из сессии
            session.commit()
            print("EUR deleted")
        else:
            print("EUR not found")

        # READ - чтобы убедиться, что удаление прошло
        stmt = select(CurrencyRates)
        for row in session.execute(stmt).scalars(): # Получаем объекты, а не строки
            print(f"ID: {row.id}, Datetime: {row.datetime}, Value: {row.value}")

