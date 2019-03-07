from rest_framework import serializers
from restapiemployee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employee_number','first_name', 'last_name','is_active')