# Generated by Django 2.2.6 on 2020-01-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest_registeration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='dispensing_pharmacist',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]