# Generated by Django 5.2.2 on 2025-06-05 11:56

import django.db.models.deletion
import tm_role.constants.permission
import tm_utils.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TMRole',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255)),
            ],
            options={
                'db_table': 'tm_role',
            },
        ),
        migrations.CreateModel(
            name='TMPermission',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('permission_type', tm_utils.models.fields.PositiveTinyIntegerField(default=tm_role.constants.permission.PermissionType['NO_ACCESS'])),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='tm_role.tmrole')),
            ],
            options={
                'db_table': 'tm_permission',
                'indexes': [models.Index(fields=['role'], name='idx_permission_role')],
            },
        ),
    ]
