# Generated by Django 3.1.6 on 2021-03-24 02:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paymentapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Billing',
            new_name='BillingAddress',
        ),
    ]