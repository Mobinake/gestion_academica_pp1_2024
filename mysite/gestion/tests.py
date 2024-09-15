from django.test import TestCase
from mysite.gestion.models import Usuario, Matricula, Materia, matricula_materia, tipo_evaluacion, Metodologia, Evaluacion


# class Rol(TestCase):
#     def test_create_new_rol(self):
#         # Create a new rol with valid inputs
#         rol = Rol.objects.create(nombre='Administrador')
#         # Check if the rol was created successfully
#         self.assertEqual(rol.nombre, 'Administrador')
#         # Check if the rol is unique
#         with self.assertRaises(Exception):
#             Rol.objects.create(nombre='Administrador')
#
#     def setUp(self):
#         Rol.objects.create(nombre='Administrador')
#
#     def test_create_rol_with_existing_name(self):
#         # Try to create a new rol with the same name
#         with self.assertRaises(Exception):
#             Rol.objects.create(nombre='Administrador')
#
#
# class Pass(TestCase):
#     def test_blank_contrasena(self):
#         # Try to create a new usuario with a blank contrasena
#         with self.assertRaises(Exception):
#             Usuario.objects.create(
#                 nombre='Test Usuario',
#                 contrasena='',
#                 estado=True,
#                 id_rol=Rol.objects.get(nombre='Administrador')
#             )
#
#     def test_invalid_contrasena_characters(self):
#         # Try to create a new usuario with an invalid contrasena (special characters)
#         with self.assertRaises(Exception):
#             Usuario.objects.create(
#                 nombre='Test Usuario',
#                 contrasena='Invalid@123',
#                 estado=True,
#                 id_rol=Rol.objects.get(nombre='Administrador')
#             )
#
#
# class Matricula(TestCase):
#     def test_create_matricula_with_negative_monto(self):
#         # Try to create a new matricula with a negative monto
#         with self.assertRaises(Exception):
#             Matricula.objects.create(
#                 detalles='Test Matricula',
#                 monto=-100,
#                 fecha=timezone.now(),
#                 id_usuario=Usuario.objects.get(nombre='Test Usuario')
#             )
#
#     def setUp(self):
#         Usuario.objects.create(
#             id_usuario=1,
#             nombre='Test Usuario',
#             contrasena='test123',
#             estado=True,
#             id_rol_id=1
#         )
#
#     def test_create_matricula_with_nonexistent_usuario(self):
#         # Try to create a new matricula with a non-existent usuario
#         with self.assertRaises(Exception):
#             Matricula.objects.create(
#                 detalles='Test Matricula',
#                 monto=1000,
#                 fecha='2022-01-01',
#                 id_usuario_id=2
#             )