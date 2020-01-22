from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomRegisterForm


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
