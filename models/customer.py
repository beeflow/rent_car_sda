"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from peewee import CharField, ForeignKeyField

from models.basemodel import BaseModel
from models.firstname import FirstName
from models.lastname import LastName


class Customer(BaseModel):
    first_name = ForeignKeyField(FirstName)
    last_name = ForeignKeyField(LastName)
    licence_id = CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
