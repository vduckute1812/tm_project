from django.db import models


class PositiveTinyIntegerField(models.PositiveSmallIntegerField):
    def db_type(self, connection):
        return "tinyint unsigned"


class TinyIntegerField(models.PositiveSmallIntegerField):
    def db_type(self, connection):
        return "tinyint"
