# Generated by Django 5.0.3 on 2024-05-17 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0004_remove_articulos_score_remove_articulos_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Articulos',
        ),
    ]
