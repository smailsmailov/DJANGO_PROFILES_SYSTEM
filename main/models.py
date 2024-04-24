from django.db import models
from django.contrib.auth.models import User , AbstractBaseUser 
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.utils.translation import gettext, gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse



class UserUpdate(models.Model):
    TYPE_OF_ACCOUNT = (
            ('seller' , 'Продавец'),
            ('worker' , 'Покупатель'),
        )
    type_of_account = models.CharField(choices=TYPE_OF_ACCOUNT , default=TYPE_OF_ACCOUNT[1])
    phone = PhoneNumberField(blank=True,default= None ,  verbose_name='Contact phone number' ,max_length=12)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
            ordering = ["user"]
            verbose_name = "Пользователь" 

    def get_type_of_account(self) : 
        dict_types = dict(self.TYPE_OF_ACCOUNT)

        return dict_types[self.type_of_account]