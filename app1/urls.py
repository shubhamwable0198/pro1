from django.urls import path
from . views import *

urlpatterns = [
    path('av/', addview ,name="add"),
    path('sv/', showview, name="show"),
    path('uv/<int:pk>/', updateview, name="update"),
    path('dv/<int:pk>/', deleteview, name="delete")

]