from django.db import models
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django import forms
# Create your models here.

User=get_user_model()
class Data_employ(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    employee_name=models.CharField(max_length=100)
    employee_email=models.CharField(max_length=100,unique=True)
    employee_contact=models.CharField(max_length=200)


'''class employ_Form(forms.ModelForm):
        class Meta:
                model = User
                fields = ["username", "email", "password"]

class employprofileform(forms.ModelForm):
        class Meta:
                model = Data_employ
                fields=['employee_contact']
'''

