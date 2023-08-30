from django.urls import path, handler404
from . import views

urlpatterns = [
    path('home/',views.index,name='index'),
    path('create/', views.create_reservation, name='create_reservation'),
    path('list/', views.list_reservations, name='list_reservations'),
]

handler404 = 'HungersBay.views.custom_404'