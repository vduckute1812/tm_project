from django.db import models


class TMRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, default="")

    class Meta:
        db_table = "tm_role"
