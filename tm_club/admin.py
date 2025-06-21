from django.contrib import admin

from tm_club.models.club import TMClub
from tm_club.models.division import TMDivision

admin.site.register(TMClub)
admin.site.register(TMDivision)
