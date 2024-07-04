# Generated by Django 5.0.4 on 2024-07-04 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_alter_period_options_remove_subject_id_schedule_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grades',
            name='evaluation_type',
            field=models.CharField(choices=[('ESC', 'Escrito'), ('ORAL', 'Oral'), ('PRAC', 'Practico'), ('MX', 'Mixto')], default='ESC', max_length=20),
        ),
        migrations.AlterField(
            model_name='grades',
            name='note',
            field=models.IntegerField(choices=[('1', 'Uno'), ('2', 'Dos'), ('3', 'Tres'), ('4', 'Cuatro'), ('5', 'Cinco')], default=None),
        ),
    ]
