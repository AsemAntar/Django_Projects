from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from users.models import Pharmacist
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
    mobile = PhoneNumberField(verbose_name='Mobile No.', max_length=15)
    insurance_company = models.CharField(
        max_length=30, choices=INSURANCE_COMPANIES, verbose_name='Insurance Company', default='bupa')
    dipensing_date = models.DateField(verbose_name='Dispensing Date')
    next_dispensing = models.DateField(verbose_name='Next Dispensing Date')
    dispensing_pharmacy = models.ForeignKey(User, on_delete=models.CASCADE)
    dispensing_pharmacist = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.fullname


class Medication(models.Model):
    DOSE = (
        ('OD', 'OD'),
        ('B.I.D', 'B.I.D'),
        ('T.I.D', 'T.I.D'),
        ('QD', 'QD'),
    )

    patient = models.ForeignKey(
        Guest, on_delete=models.CASCADE, related_name='medications')

    name = models.CharField(
        max_length=250, verbose_name='Medicine', blank=True)

    dose = models.CharField(
        max_length=8, verbose_name='Dose', choices=DOSE, blank=True)

    frequency = models.IntegerField(
        choices=[(1, 1), (2, 2), (3, 3), (4, 4)], verbose_name='Frequency', blank=True)

    quantity = models.IntegerField(verbose_name='Number of boxes', blank=True)

    def __str__(self):
        return self.name.upper()


class Prescription(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)

    dispensing_date = models.DateTimeField(
        default=timezone.now, verbose_name='Dispensing Date')

    dispensing_period = models.PositiveIntegerField(
        verbose_name='Duration')

    def calculate_date(self):
        next_date = timezone.now() + timedelta(days=self.dispensing_period)
        return next_date

    next_dispensing = models.DateTimeField(default=)
