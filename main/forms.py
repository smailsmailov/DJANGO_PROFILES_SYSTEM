from django.forms import forms , CharField , DateField , Select , PasswordInput
from .models import UserUpdate
from django.utils.translation import gettext as _
from django.contrib.auth.models import User 


class UserForm(forms.Form):
    username = CharField(label=_("Your nickname"), max_length=100)
    first_name = CharField(label=_("Your first name"), max_length=100)
    last_name = CharField(label=_("Your last name"), max_length=100)
    date_of_birth = DateField(label=_("Your date of birth"))    
    is_staff = CharField(widget=Select(choices=UserUpdate.TYPE_OF_ACCOUNT))
    password = CharField(widget=PasswordInput())
    phone = CharField(max_length=11)