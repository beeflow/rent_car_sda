"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from datetime import datetime

from peewee import ForeignKeyField, DateTimeField, IntegerField

from models.basemodel import BaseModel
from models.car import Car
from models.customer import Customer


class RentCar(BaseModel):
    """Na tabeli jest trigger sprawdzający i zmieniający status wypożyczenia pojazdu."""
    car = ForeignKeyField(Car)
    customer = ForeignKeyField(Customer)
    rent_time = DateTimeField(null=False, default=datetime.now())
    return_time = DateTimeField(null=True)
    is_active = IntegerField(null=False, default=1)

    def __str__(self):
        return f"{self.car.register_number} rent by: {self.customer} " \
               f"on {self.rent_time} " \
               f"returned: {self.return_time if self.return_time else ''}"
