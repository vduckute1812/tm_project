from django.contrib.auth.models import User
from django.db import models

from tm_meeting.constants.meeting import MeetingRole
from tm_meeting.models import TMSession
from tm_utils.models.fields import PositiveTinyIntegerField
from toastmaster import settings


class TMSpeech(models.Model):
    id = models.BigAutoField(primary_key=True)
    speaker = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="speeches", on_delete=models.CASCADE, null=True)
    session = models.ForeignKey(TMSession, related_name="speeches", on_delete=models.CASCADE)
    role = PositiveTinyIntegerField(default=MeetingRole.UNKNOWN)

    class Meta:
        db_table = "tm_speech"
        indexes = [
            models.Index(fields=['session'], name='idx_speech_session'),
            models.Index(fields=['speaker'], name='idx_speech_speaker'),
        ]
