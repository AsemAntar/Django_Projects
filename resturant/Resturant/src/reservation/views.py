from django.shortcuts import render
from .models import Reservation


def reserve_table(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations,
    }

    return render(request, 'reservation/reservation.html', context)
