# Generated by Django 5.0.4 on 2024-07-03 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user', 'ci'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='id_user',
            new_name='user',
        ),
    ]