# Generated by Django 2.2.6 on 2020-04-03 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
