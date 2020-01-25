from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'


class Pharmacist(models.Model):
    working_at = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Pharmacist Name')
    emp_code = models.CharField(max_length=6, verbose_name='Employee Code')

    def __str__(self):
        return self.name + '(' + self.emp_code + ')' + f'(working at {self.working_at})'
