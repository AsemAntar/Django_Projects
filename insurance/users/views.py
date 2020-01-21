from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register_users(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Account created for {username}!')
            return redirect('guest_registeration:guest_list')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register_users.html', {'form': form})
