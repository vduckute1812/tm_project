from django.contrib import admin
from tm_meeting.models import TMMeeting, TMSession, TMSpeech

admin.site.register(TMMeeting)
admin.site.register(TMSession)
admin.site.register(TMSpeech)