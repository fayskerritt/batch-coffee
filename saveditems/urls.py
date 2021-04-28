from django.urls import path
from . import views

urlpatterns = [
    path('', views.saved_items, name='saved_items'),
]
