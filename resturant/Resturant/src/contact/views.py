from os import environ
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ContactUsForm


def send_email(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'A message from {name} with Phonenumber {phone}', message, from_email,
                          [environ.get('EMAIL_USER')])
                messages.success(
                    request, 'Your email was sent successfully ^_^')
            except BadHeaderError:
                return HttpResponse('Invalid Header')
        return redirect('contact_us:send_email')
    else:
        form = ContactUsForm()
        context = {'form': form}
        return render(request, 'contact/contact.html', context)
