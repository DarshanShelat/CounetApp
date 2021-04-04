from django.contrib import admin
from django.urls import path
from .views import helloworld, Increment, Decrement, Reset

urlpatterns = [
    path('helloworld/', helloworld),
    path('Increment/', Increment),
    path('Decrement/', Decrement),
    path('Reset/', Reset),
]
