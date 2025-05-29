from authtools.models import User
from django.db import models
from tm_channel.models.channel import TMChannel


class TMChannelUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='channel_users')
    channel = models.ForeignKey(TMChannel, on_delete=models.CASCADE, related_name='channel_users')
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "tm_channel_users"
        unique_together = (("channel_id", "user_id"),)
