from django.db import models

from authtools.models import User

from tm_channel.constants.channel import MessageStatus
from tm_channel.models.channel import TMChannel
from tm_utils.models.abstract import TimeStampedModel
from tm_utils.models.fields import PositiveTinyIntegerField


class TMMessage(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    channel = models.ForeignKey(TMChannel, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = PositiveTinyIntegerField(default=MessageStatus.SENT)

    class Meta:
        db_table = "tm_channels"
