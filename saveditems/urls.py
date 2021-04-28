from django.urls import path
from . import views

urlpatterns = [
    path('', views.saved_items, name='saved_items'),
    path('add_save/<product_id>', views.add_save, name='add_save'),
]
