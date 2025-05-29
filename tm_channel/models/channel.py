from django.db import models

from tm_channel.constants.channel import ChannelType, ChannelStatus
from tm_utils.models.abstract import TimeStampedModel
from tm_utils.models.fields import PositiveTinyIntegerField


class TMChannel(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    channel_type = PositiveTinyIntegerField(default=ChannelType.DEFAULT)
    status = PositiveTinyIntegerField(default=ChannelStatus.ACTIVE)

    class Meta:
        db_table = "tm_channels"

    def __str__(self):
        return self.name

    def is_active(self):
        return self.status == ChannelStatus.ACTIVE
