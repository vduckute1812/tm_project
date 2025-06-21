from django.db import models
from tm_club.models import TMClub


class TMRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, default="")
    club = models.ForeignKey(
        TMClub,
        related_name="roles",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "tm_role"
        indexes = [models.Index(fields=['club'], name='idx_role_club')]
