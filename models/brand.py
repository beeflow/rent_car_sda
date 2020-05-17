"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from peewee import CharField

from .basemodel import BaseModel


class Brand(BaseModel):
    name = CharField(max_length=25, null=False, unique=True)

    def __str__(self):
        return self.name
