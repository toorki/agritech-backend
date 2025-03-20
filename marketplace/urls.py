from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_produce),
    path('buy/', views.buy_produce),
    path('all/', views.list_all_produce),
]