from django.db import models

from tm_club.models.division import TMDivision
from tm_utils.models.abstract import TimeStampedModel


class TMClub(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, default="")
    division = models.ForeignKey(TMDivision, related_name="clubs", on_delete=models.CASCADE)

    class Meta:
        db_table = "tm_club"
        models.Index(fields=['division'], name='idx_club_division'),
