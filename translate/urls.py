from .views import *
from django.urls import path

app_name = 'translate'

urlpatterns = [
    path('', home, name='home'),
    path('info/', info, name='info')
]
