from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Pharmacy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pharmacy_code = models.CharField(
        max_length=6, verbose_name='Pharmacy Code')
    pharmacy_name = models.CharField(
        max_length=50, verbose_name='Pharmacy Name')

    def __str__(self):
        return self.pharmacy_name + ' ' + '(' + self.pharmacy_code + ')'


class Pharmacist(models.Model):
    pharmacist_name = models.CharField(
        max_length=200, verbose_name='Pharmacist Name')
    pharmacist_code = models.CharField(
        max_length=10, verbose_name='Employee Code')
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)

    def __str__(self):
        return self.pharmacist_name + ' ' + '(' + self.pharmacist_code + ')'


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
    dispensing_pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    dispensing_pharmacist = models.ForeignKey(
        Pharmacist, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.fullname
