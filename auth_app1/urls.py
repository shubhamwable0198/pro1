from django.urls import path
from .views import *

urlpatterns = [
    path('suv/', signupview, name="sign"),
    path('lv/', loginview, name="login"),
    path('lo/', logoutview, name="logout")
]