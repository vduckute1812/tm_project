from django.db import models

from tm_role.constants.permission import PermissionType
from tm_role.models.role import TMRole
from tm_utils.models.fields import PositiveTinyIntegerField

class TMPermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.ForeignKey(TMRole, related_name="permissions", on_delete=models.CASCADE)
    permission_type = PositiveTinyIntegerField(default=PermissionType.NO_ACCESS)

    class Meta:
        db_table = "tm_permission"
        indexes = [models.Index(fields=['role'], name='idx_permission_role')]
