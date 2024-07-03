from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist
from .models import *


@receiver(post_save, sender=Profile)
def add_user_to_students_group(sender, instance, created, **kwargs):
    # agregar automaticamente el estudiante creado al grupo de estudiantes
    if created:
        try:
            students = Group.objects.get(name='students')
        except ObjectDoesNotExist:
            students = Group.objects.create(name='students')
        instance.user.groups.add(students)

    Group.objects.get_or_create(name='teachers')
    Group.objects.get_or_create(name='admins')
