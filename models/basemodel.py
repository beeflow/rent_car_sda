"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""

from peewee import *

from settings import DATABASE_CONFIG, DATABASE_NAME

mysql = MySQLDatabase(DATABASE_NAME, **DATABASE_CONFIG)


class BaseModel(Model):
    class Meta:
        database = mysql
        legacy_table_names = False

    id = AutoField()
