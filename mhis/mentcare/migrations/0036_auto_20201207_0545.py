# Generated by Django 3.1.1 on 2020-12-07 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentcare', '0035_prescription'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prescription',
            new_name='Prescriptions',
        ),
    ]
