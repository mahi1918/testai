from django.urls import path
import execute_tests
from . import views

urlpatterns = [
    path('tests/v1/execute', views.list_tests, name="list-tests"),
    path('execute', views.check_endpoint, name='check_endpoint'),
]