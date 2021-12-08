from django.db import models

# Create your models here.

CHOICES= (
    ('Java Developer','JAVA DEVELOPER'),
    ('Software Tester', 'SOFTWARE TESTER'),
    ('Python Developer','PYTHON DEVELOPER'),
    ('Manager','MANAGER'),
)


class Employee(models.Model):
    employee_name            =models.CharField(max_length=100)
    employee_designation     =models.CharField(max_length=100)
    employee_salary          =models.FloatField()
    employee_age             =models.IntegerField()
    employee_email_id        =models.EmailField()
    employee_address         =models.CharField(max_length=100)
    employee_gender          =models.CharField(max_length=100)

    def __str__(self):
        return self.employee_name
        
    employee_designation       =models.CharField(max_length=100, choices=CHOICES, default='Select Designation')
    
    

    
