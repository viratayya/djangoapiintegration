from django.db import models

# Create your models here.
#  Last name, First name and Employee Number


class Employee(models.Model):

    employee_number = models.CharField(primary_key=True, db_column='Employee Number', max_length=32)  # 429,49,67,296 possible id.

    first_name = models.CharField(db_column='First Name', max_length=50)  

    last_name = models.CharField(db_column='Last Name', max_length=32) 
  
    is_active = models.BooleanField(default=True,db_column='Is Active')

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name