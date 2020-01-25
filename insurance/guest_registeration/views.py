from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import GuestRegisterForm, MedicationForm
from .models import Guest, Medication


def guest_list(request):
    context = {'guest_list': Guest.objects.all()}
    return render(request, 'guest_registeration/guest_list.html', context)


@login_required
def guest_register(request, id=0):
    new_guest = None
    if request.method == 'POST':
        if id == 0:
            form = GuestRegisterForm(data=request.POST)
        else:
            guest = Guest.objects.get(pk=id)
            form = GuestRegisterForm(request.POST, instance=guest)
        if form.is_valid():
            new_guest = form.save(commit=False)
            new_guest.dispensing_pharmacy = request.user
            new_guest.save()
        return redirect('guest_registeration:guest_list')
    else:
        if id == 0:
            form = GuestRegisterForm()
        else:
            guest = Guest.objects.get(pk=id)
            form = GuestRegisterForm(instance=guest)
        return render(request, 'guest_registeration/register.html', {'form': form})


@login_required
def guest_delete(request, id):
    guest = Guest.objects.get(pk=id)
    guest.delete()
    return redirect('guest_registeration:guest_list')


@login_required
def guest_detail(request, id):
    guest = Guest.objects.get(pk=id)

    # get list of medications for the current guest
    drugs = guest.medications.all()

    # add new drug
    new_drug = None

    if request.method == 'POST':
        med_form = MedicationForm(data=request.POST)
        if med_form.is_valid():
            new_drug = med_form.save(commit=False)
            new_drug.patient = guest
            new_drug.save()
        return redirect('guest_registeration:guest_detail', id=id)
    else:
        med_form = MedicationForm()
        return render(request, 'guest_registeration/detail.html', {'guest': guest, 'drugs': drugs, 'med_form': med_form})
