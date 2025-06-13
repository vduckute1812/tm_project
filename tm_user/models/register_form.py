from datetime import datetime

from django.db import models
from authtools.models import User

from tm_user.constants.toastmaster import VerificationType
from tm_utils.models.abstract import TimeStampedModel
from tm_utils.models.fields import PositiveTinyIntegerField


class TMRegisterForm(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, unique=True)
    verify_code = models.CharField(max_length=6)
    expired_at = models.DateTimeField(auto_now=False)
    token_expired_at = models.DateTimeField(auto_now=False)
    verification_type = PositiveTinyIntegerField(default=VerificationType.NEW_GUEST)

    class Meta:
        db_table = "tm_register_form"
        indexes = [
            models.Index(fields=['token'], name='idx_register_form_token'),
            models.Index(fields=['user'], name='idx_register_form_user'),
        ]

    @property
    def is_expired(self) -> bool:
        return not self.expired_at or self.expired_at < datetime.now()

    @property
    def is_token_expired(self) -> bool:
        return not self.token_expired_at or self.token_expired_at < datetime.now()
