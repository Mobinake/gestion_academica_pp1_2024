# Generated by Django 5.0.3 on 2024-05-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0002_articulos_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulos',
            name='text',
            field=models.CharField(max_length=100, null=True),
        ),
    ]