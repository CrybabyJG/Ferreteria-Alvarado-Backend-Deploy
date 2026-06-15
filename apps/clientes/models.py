from django.db import models

# Create your models here.

class Clientes(models.Model):
    ID_Cliente = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=20, verbose_name='Nombres*')
    Telefono = models.CharField(max_length=12, verbose_name='Teléfono*')
    Correo = models.EmailField(verbose_name='Correo*')
    Fecha_Registro = models.DateField(verbose_name='Fecha Registro*')
    Origen = models.CharField(max_length=50, verbose_name='Origen*')
    Interes = models.CharField(max_length=150, verbose_name='Interes*')

    class Meta:
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.Nombres}  {self.Telefono}  {self.Correo}  {self.Fecha_Registro}  {self.Origen}  {self.Interes}'