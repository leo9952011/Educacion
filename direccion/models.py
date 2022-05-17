
from django.db import models

# Create your models here.

# -------- Pais - Pcia - Ciudad -------------------
class Pais(models.Model):
    nombrePais = models.CharField(max_length=60)
    class meta:
        verbose_name = "Pais"
        verbose_plural_name = "Paises"
    def __str__(self):
        return self.nombrePais

class Provincia(models.Model):
    nombreProvincia = models.CharField(max_length=60)
    Pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    class meta:
        verbose_name = "Provincia"
        verbose_plural_name = "Provincias"
    def __str__(self):
        return self.nombreProvincia

class Ciudad(models.Model):
    nombreCiudad = models.CharField(max_length=60)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)
    class meta:
        verbose_name = "Ciudad"
        verbose_plural_name = "Ciudades"
    def __str__(self):
        return self.nombreCiudad


# --------- Tipos de cargo

class TipoCargo(models.Model):
    detalle = models.CharField(max_length=60)
    class Meta:
        verbose_name = "tipo de cargo"
        verbose_plural_name = "Tipos de cargos"
    def __str__(self):
        return self.detalle

# -------- Persona - Alumno - Profesor - Auxiliar - Cargo ---------

class Persona(models.Model):
    dni = models.IntegerField()
    nombrePersona = models.CharField(max_length=60)
    apellidoPersona = models.CharField(max_length=60)
    fechaNac = models.DateField()
    email = models.EmailField()
    tel = models.CharField(max_length=12)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)

class Alumno(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Alumno"
        verbose_plural_name = "Alumnos"

class Profesor(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    #asignatura = models.ForeignKey(asignatura, on_delete=models.PROTECT) # Crear asignatura
    class Meta:
        verbose_name = "Profesor"
        verbose_plural_name = "Profesores"

class Auxiliar(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Auxiliar"
        verbose_plural_name = "Auxiliares"

class Cargo(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    tipo = models.ForeignKey(TipoCargo, on_delete=models.PROTECT)
    turno = models.CharField(max_length=30)
    class Meta:
        verbose_name = "Cargo"
        verbose_plural_name = "Cargos"


# -------------- Asignatura
class Asignatura(models.Model):
    detalle = models.CharField(max_length=60)
    promocionable = models.BooleanField(default=False)
    matricula = models.ManyToManyField(Alumno)
    #carrera
    #curso