import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):
    """
        Бул Product модели биздин база данных моделине керек
    """
    __tablename__ = "product"
    id  = sa.Column(sa.Integer, primary_key=True, index=True) # primary key - Бул id уникалдуу, 
    name = sa.Column(sa.String(50))
    price = sa.Column(sa.Integer)
    description = sa.Column(sa.String(50))

    def __str__(self):
        return f"name: {self.name}" 

# Product id: 1 name: Футбол Топу price: 250 
# request = name: Футбол топу,  price  250z 

