from django.urls import path
from . import views
# import views

urlpatterns = [
    path('', views.index),
    path('new' , views.new)
]