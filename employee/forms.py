from django import forms

class form_employ(forms.Form):
    employee_name=forms.CharField(max_length=100)
    employee_email=forms.EmailField(max_length=100)
    employee_contact=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)