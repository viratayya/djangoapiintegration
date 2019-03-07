from django.urls import path, include 
from restapiemployee.views import EmployeeViewSet
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet, )

urlpatterns = [
    path('v1/', include((router.urls,'restapi'),namespace='restapi')),
]
