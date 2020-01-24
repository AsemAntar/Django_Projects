from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CustomRegisterForm, PharmacistForm
from .models import Pharmacist, Profile


def register_users(request):
    if request.method == 'POST':
        form = CustomRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your account has been created. You are able to login now!')
            return redirect('users:login')
    else:
        form = CustomRegisterForm()
    return render(request, 'users/register_users.html', {'form': form})


@login_required
def profile(request):
    # get all pharmacists of the current user
    pharmacists = Pharmacist.objects.filter(working_at=request.user)
    # get the current user
    current_user = request.user
    new_pharmacist = None
    if request.method == 'POST':
        form = PharmacistForm(data=request.POST)
        if form.is_valid():
            new_pharmacist = form.save(commit=False)
            new_pharmacist.working_at = current_user
            new_pharmacist.save()
        return redirect('users:profile')
    else:
        form = PharmacistForm()
    return render(request, 'users/profile.html', {'form': form, 'pharmacists': pharmacists})


@login_required
def pharmacist_delete(request, id):
    pharmacist = Pharmacist.objects.filter(working_at=request.user).get(pk=id)
    pharmacist.delete()
    return redirect('users:profile')
