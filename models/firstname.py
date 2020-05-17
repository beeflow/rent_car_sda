"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from peewee import CharField

from models.basemodel import BaseModel


class FirstName(BaseModel):
    name = CharField(max_length=15, null=False, unique=True)

    def __str__(self):
        return self.name
