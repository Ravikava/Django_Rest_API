from django.db import models


class Employee(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_mobile = models.CharField(max_length=10)
    emp_city = models.CharField(max_length=15)
    
    def __str__(self):
        return self.emp_name