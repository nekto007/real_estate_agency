# Generated by Django 2.2.24 on 2023-05-13 21:44

import phonenumbers
from django.db import migrations


def normalized_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    if flats.exists():
        for flat in flats.iterator():
            pure_phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
            if phonenumbers.is_valid_number(pure_phonenumber):
                flat.owner_pure_phone = pure_phonenumber
                flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0010_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalized_phone_number),
    ]
