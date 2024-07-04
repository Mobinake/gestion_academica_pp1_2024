# Generated by Django 5.0.4 on 2024-07-04 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_remove_subject_id_teacher_remove_teacher_id_subject_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grades',
            options={'ordering': ['id_student', 'id_student', 'note'], 'verbose_name': 'Calificación', 'verbose_name_plural': 'Calificaciones'},
        ),
        migrations.AlterModelOptions(
            name='period',
            options={'ordering': ['id_period', 'name_period', 'year_period'], 'verbose_name': 'Periodo Academico', 'verbose_name_plural': 'Periodos Academicos'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['ci', 'first_name', 'last_name'], 'verbose_name': 'Persona', 'verbose_name_plural': 'Personas'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user', 'ci', 'name_user'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['id_subject', 'name_subject'], 'verbose_name': 'Asignatura', 'verbose_name_plural': 'Asignaturas'},
        ),
    ]
