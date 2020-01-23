from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Guest(models.Model):
    INSURANCE_COMPANIES = (
        ('Bupa', 'Bupa'),
        ('MedGulf', 'MedGulf'),
        ('MedNet', 'MedNet'),
        ('Tawnyia', 'Tawnyia'),
        ('Saudi Enaya', 'Saudi Enaya'),
    )
    fullname = models.CharField(max_length=250, verbose_name='Full Name')
    mobile = PhoneNumberField(verbose_name='Mobile No.')
    insurance_company = models.CharField(
        max_length=30, choices=INSURANCE_COMPANIES, verbose_name='Insurance Company', default='bupa')
    dipensing_date = models.DateField(verbose_name='Dispensing Date')
    next_dispensing = models.DateField(verbose_name='Next Dispensing Date')
    dispensing_pharmacy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname
