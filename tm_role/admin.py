from django.contrib import admin

from tm_club.models import TMDivision, TMClub
from tm_meeting.models import TMMeeting, TMSession, TMSpeech
from tm_role.models import TMRole, TMPermission
from tm_user.models import TMGuest, TMToastMaster
from tm_user.models.register_form import TMRegisterForm
from tm_user.models.user_auth import TMUserAuth

# Register your models here.

admin.site.register(TMClub)
admin.site.register(TMDivision)

admin.site.register(TMMeeting)
admin.site.register(TMSession)
admin.site.register(TMSpeech)

admin.site.register(TMRole)
admin.site.register(TMPermission)

admin.site.register(TMGuest)
admin.site.register(TMToastMaster)
admin.site.register(TMRegisterForm)
admin.site.register(TMUserAuth)
