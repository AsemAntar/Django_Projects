from django.shortcuts import render, redirect
from .forms import GuestRegisterForm
from .models import Guest


def guest_list(request):
    context = {'guest_list': Guest.objects.all()}
    return render(request, 'guest_registeration/guest_list.html', context)


def guest_register(request, id=0):
    if request.method == 'POST':
        if id == 0:
            form = GuestRegisterForm(data=request.POST)
        else:
            guest = Guest.objects.get(pk=id)
            form = GuestRegisterForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
        return redirect('guest_registeration:guest_list')
    else:
        if id == 0:
            form = GuestRegisterForm()
        else:
            guest = Guest.objects.get(pk=id)
            form = GuestRegisterForm(instance=guest)
        return render(request, 'guest_registeration/register.html', {'form': form})


def guest_delete(request, id):
    guest = Guest.objects.get(pk=id)
    guest.delete()
    return redirect('guest_registeration:guest_list')


def guest_detail(request, id):
    context = {'guest': Guest.objects.get(pk=id)}
    return render(request, 'guest_registeration/detail.html', context)
