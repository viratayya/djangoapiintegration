

from rest_framework import viewsets
from restapiemployee.models import Employee
from restapiemployee.serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    logging_methods = ['POST']


