# Generated by Django 3.2.18 on 2023-09-14 17:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Liked_by',
            field=models.ManyToManyField(blank=True, related_name='Liked_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]