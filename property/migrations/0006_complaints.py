# Generated by Django 2.2.24 on 2023-05-11 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_auto_20230511_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Текст жалобы:')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Flat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
