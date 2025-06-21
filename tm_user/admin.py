from django.contrib import admin
from tm_user.models import TMGuest, TMToastMaster
from tm_user.models.register_form import TMRegisterForm
from tm_user.models.user_auth import TMUserAuth

admin.site.register(TMGuest)
admin.site.register(TMToastMaster)
admin.site.register(TMRegisterForm)
admin.site.register(TMUserAuth)
