"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""

from peewee import CharField, ForeignKeyField

from .basemodel import BaseModel
from .brand import Brand


class CarModel(BaseModel):
    class Meta:
        table_name = 'model'

    name = CharField(max_length=50, null=False)
    brand = ForeignKeyField(Brand)

    def __str__(self):
        return f"{self.brand} {self.name}"
