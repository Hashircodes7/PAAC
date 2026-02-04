from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
   
    age=models.IntegerField(null=False,blank=False)
    department_choices=[('finance','Finance'),('hr','HR'),('marketing','Marketing'),('engineering','Engineering'),('staff','Staff')]
    department=models.CharField(max_length=15,choices=department_choices)
    role_choices=[('intern','Intern'),('employee','Employee'),('manager','Manager'),('ceo','CEO'),('auditor','Auditor')]
    role=models.CharField(max_length=15,choices=role_choices)
    experience=models.FloatField(null=False,blank=False)
    trust_score= models.IntegerField(null=False,blank=False)
    is_active=models.BooleanField(default=True)
    
    REQUIRED_FIELDS=[
        'department','age','role','experience','trust_score'
    ]

    def __str__(self):
        return self.username
    