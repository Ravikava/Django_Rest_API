from rest_framework import serializers
from Api_app.models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'emp_name', 'emp_mobile','emp_city']