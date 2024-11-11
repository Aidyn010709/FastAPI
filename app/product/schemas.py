from pydantic import BaseModel

class ProductSchema(BaseModel):
    name: str
    price: int
    description: str

    class Config:
        from_attributes = True

                      # Validation

# SQL DATABASE      # Pydantic           # JSON Response
# Product  
# name      ->         str(Name)        -> Футбол топу
# price     ->         int(Price)   ->     250
# description   ->     str(Description)  ->  Топ футбол для тренировки


# 010010101001 -> Футбол топу