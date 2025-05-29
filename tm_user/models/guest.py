from authtools.models import User
from django.db import models

from tm_utils.models.abstract import TimeStampedModel


class TMGuest(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, default="")
    phone_number = models.CharField(max_length=64, default="")

    class Meta:
        db_table = "tm_guest"
        indexes = [models.Index(fields=['user'], name='idx_guest')]
