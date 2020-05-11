from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReserveTableForm


def reserve_table(request):
    if request.method == 'POST':
        reservation_form = ReserveTableForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
    else:
        reservation_form = ReserveTableForm()
        return render(request, 'reservation/reservation.html', {
            'reservation_form': reservation_form,
        })

    return redirect('reservation:reserve_table')
