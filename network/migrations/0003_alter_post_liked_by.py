# Generated by Django 3.2.18 on 2023-09-14 17:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_auto_20230914_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
