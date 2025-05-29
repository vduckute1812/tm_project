from django.db import models

from tm_meeting.constants.meeting import SessionType
from tm_meeting.models import TMMeeting
from tm_utils.models.fields import PositiveTinyIntegerField


class TMSession(models.Model):
    id = models.BigAutoField(primary_key=True)
    meeting = models.ForeignKey(TMMeeting, related_name="sessions", on_delete=models.CASCADE)
    type = PositiveTinyIntegerField(default=SessionType.UNKNOWN)

    class Meta:
        db_name = "tm_session"
        indexes = [models.Index(fields=['meeting'], name='idx_session_meeting')]
