# Generated by Django 3.2.7 on 2022-01-17 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='slug',
        ),
    ]
