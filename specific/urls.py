from specific.views import *
from django.urls import path

app_name='something'

urlpatterns=[
    path('keerthana/',keerthana,name='keerthana'),
    path('jacintha/',jacintha,name='jacintha'),
]