from django.urls import path
from . import views

urlpatterns = [
    path('flights/', views.flight_list, name='flight_list'),
    path('flights/<int:flight_id>/', views.flight_detail, name='flight_detail'),
    path('flights/<int:flight_id>/book/', views.book_ticket, name='book_ticket'),
    path('my-tickets/', views.my_tickets, name='my_tickets'),
]
