# Generated by Django 5.0.4 on 2024-06-26 19:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0011_alter_person_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
