from django.db import models
from authtools.models import User

from tm_club.models import TMClub
from tm_user.constants.toastmaster import Level
from tm_utils.models.abstract import TimeStampedModel
from tm_utils.models.fields import PositiveTinyIntegerField


class TMToastMaster(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, default="")
    phone_number = models.CharField(max_length=64, default="")
    club = models.ForeignKey(TMClub, on_delete=models.CASCADE, related_name="toastmasters", null=True)
    level = PositiveTinyIntegerField(default=Level.UNKNOWN)

    class Meta:
        db_table = "tm_toastmaster"
        indexes = [
            models.Index(fields=['user'], name='idx_toastmaster'),
            models.Index(fields=['club'], name='idx_toastmaster_club'),
        ]
