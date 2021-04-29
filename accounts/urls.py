from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    path('account_details/', views.account_details, name='account_details'),
    path('account_orders/', views.account_orders, name='account_orders'),
]
