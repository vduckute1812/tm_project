from django.db import models

from tm_user.models import TMClub
from tm_utils.models.abstract import TimeStampedModel
from tm_utils.models.fields import PositiveTinyIntegerField


class TMMeeting(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    club = models.ForeignKey(TMClub, on_delete=models.SET_NULL, null=True)
    topic = models.CharField(max_length=255, default="")
    date = models.DateTimeField(default=None, null=True)
    address = models.CharField(max_length=255, default="")
    number = PositiveTinyIntegerField()

    class Meta:
        db_name = "tm_meeting"
        indexes = [models.Index(fields=['club'], name='idx_meeting_club')]
