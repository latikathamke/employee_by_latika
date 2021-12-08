from django import forms
from empapp.models import Employee

GENDER_CHOICES=[('male','Male'),
                ('female','Female'),
                 ('other','Other'),
                ]


class AddEmployeeForm(forms.ModelForm):
    employee_gender    = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model   =Employee
        fields=['employee_name','employee_designation','employee_salary','employee_age','employee_email_id','employee_address','employee_gender']


class UpdateEmployeeForm(forms.ModelForm):
    employee_gender    = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model   =Employee
        fields=['employee_name','employee_designation','employee_salary','employee_age','employee_email_id','employee_address','employee_gender']