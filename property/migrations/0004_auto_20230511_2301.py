# Generated by Django 2.2.24 on 2023-05-11 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(db_index=True, null=True, verbose_name='New building'),
        ),
    ]
