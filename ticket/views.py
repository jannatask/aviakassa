from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Flight, Passenger, Ticket
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils import timezone

# Представление для списка рейсов
def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flights/list.html', {'flights': flights})

# Представление для детальной информации о рейсе
def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    return render(request, 'flights/detail.html', {'flight': flight})

# Представление для бронирования билета
@login_required
def book_ticket(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    passenger, created = Passenger.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        # Здесь может быть логика проверки доступности мест и т.д.
        Ticket.objects.create(flight=flight, passenger=passenger, purchase_date=timezone.now())
        return redirect('flight_list')  # Перенаправление на список рейсов после покупки
    return render(request, 'flights/book.html', {'flight': flight})

# Представление для отображения билетов пользователя
@login_required
def my_tickets(request):
    passenger = get_object_or_404(Passenger, user=request.user)
    tickets = passenger.tickets.all()
    return render(request, 'flights/my_tickets.html', {'tickets': tickets})


