from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(('restapiemployee.urls','restapiemployee'), namespace='restapiemployee')),
    path('posts/',include(('apiintegration.urls','apiintegration'),namespace='restapiemployee')),
]


