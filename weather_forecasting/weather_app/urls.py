from django.urls import path
from . import views

urlpatterns=[
    path('info/',views.abc, name='abc')
]