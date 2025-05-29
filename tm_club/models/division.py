from django.db import models

from tm_utils.models.abstract import TimeStampedModel


class TMDivision(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, default="")

    class Meta:
        db_table = "tm_division"
