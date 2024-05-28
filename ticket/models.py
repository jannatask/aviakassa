from django.db import models

from django.contrib.auth.models import User

# Модель для представления авиарейса
class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    departure_airport = models.CharField(max_length=100)
    arrival_airport = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.flight_number} from {self.departure_airport} to {self.arrival_airport}"

# Модель для представления пассажира
class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    passport_number = models.CharField(max_length=9)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

# Модель для представления покупки билета
class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='tickets')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='tickets')
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket for {self.passenger} on flight {self.flight.flight_number}"

