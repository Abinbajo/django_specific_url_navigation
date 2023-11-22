
from django.urls import path 
from app1.views import *

app_name='a'


urlpatterns = [
    path('abin/',abin, name='abin'),
]

