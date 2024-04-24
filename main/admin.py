from django.contrib import admin
from .models import *
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserDInline(admin.StackedInline):
    model = UserUpdate
    can_delete = False
    verbose_name_plural = _('Required fields')


class UserAdmin(BaseUserAdmin):
    inlines = (UserDInline,)
    list_display = ('username','email','last_name','first_name', )
    search_fields = ('username' , 'last_name' , 'first_name')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)