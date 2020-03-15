from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def pricing(request):
    return render(request, 'pricing.html')


def service(request):
    return render(request, 'service.html')


def contact(request):

    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        # send an email
        send_mail(
            message_name, message, message_email, [
                'asemtestforweb@gmail.com', 'asemantar@gmail.com']
        )

        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html')


def appointment(request):

    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_time = request.POST['your-time']
        your_message = request.POST['your-message']

        '''
        # send an email
        send_mail(
            message_name, message, message_email, [
                'asemtestforweb@gmail.com', 'asemantar@gmail.com']
        )
        '''
        return render(request, 'appointment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_time': your_time,
            'your_message': your_message,
        })
    else:
        return render(request, 'home.html')
