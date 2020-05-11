from django import forms
from .models import Reservation


class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', }),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', }),
        #     'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', }),
        #     'number_of_persons': forms.NumberInput(attrs={'class': 'form-control', 'id': 'persons'}),
        #     'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'date', }),
        #     'time': forms.TimeInput(attrs={'class': 'form-control', 'id': 'time', }),
        # }
