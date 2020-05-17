"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from peewee import ForeignKeyField, CharField, IntegerField

from models.basemodel import BaseModel
from models.brand import Brand
from models.carmodel import CarModel
from models.carstatus import CarStatus


class Car(BaseModel):
    brand = ForeignKeyField(Brand)
    model = ForeignKeyField(CarModel)
    register_number = CharField(max_length=10, null=True)
    production_year = IntegerField(null=True)
    status = ForeignKeyField(CarStatus)

    def __str__(self):
        return f'{self.model} - {self.register_number}'
