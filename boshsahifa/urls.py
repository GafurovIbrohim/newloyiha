from django.urls import path
from .views import boshsahifaView

urlpatterns=[
    path('',boshsahifaView, name='home')
]