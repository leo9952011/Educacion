
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
    class meta:
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
    class meta:
        verbose_name = "Alumno"
        verbose_plural_name = "Alumnos"

class Profesor(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    class meta:
        verbose_name = "Profesor"
        verbose_plural_name = "Profesores"

class Auxiliar(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    class meta:
        verbose_name = "Auxiliar"
        verbose_plural_name = "Auxiliares"

class Cargo(models.Model):
    options = [
        (1, 'Mañana'),
        (2, 'Tarde'),
        (3, 'Noche')
    ]
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    tipo = models.ForeignKey(TipoCargo, on_delete=models.PROTECT)
    turno = models.CharField(max_length=30)
    class meta:
        verbose_name = "Cargo"
        verbose_plural_name = "Cargos"


# --------------Carrera y tipo de carrera - Curso - Asignatura

class TipoCarrera(models.Model):
    detalle = models.CharField(max_length=60)
    class meta:
        verbose_name = "Tipo de carrera"
        verbose_plural_name = "Tipos de carreras"

class Carrera(models.Model):
    tipo = models.ForeignKey(TipoCarrera, on_delete=models.PROTECT)
    detalle = models.CharField(max_length=60)
    class meta:
        verbose_name = "Carrera"
        verbose_plural_name = "Carreras"

class Curso(models.Model):
    angno = models.CharField(max_length=10)
    detalle = models.CharField(max_length=60)
    class meta:
        verbose_name = "Curso"
        verbose_plural_name = "Cursos"

class Asignatura(models.Model):
    detalle = models.CharField(max_length=60)
    promocionable = models.BooleanField(default=False)
    matricula = models.ManyToManyField(Alumno)
    carrera = models.ForeignKey(Carrera, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    profesor = models.ForeignKey(Profesor, on_delete=models.PROTECT)
    class meta:
        verbose_name = "Asignatura"
        verbose_plural_name = "Asignaturas"


# -------------- Calificación - Tipo de calificación
"""
class TipoCalificacion(models.Model):
    detalle = models.CharField(max_length=60)
    class meta:
        verbose_name = "Tipo de califición"
        verbose_plural_name = "Tipos de calificacines"
"""

class Calificacion(models.Model):
    options = [
        (1, 'Parcial'),
        (2, 'Recuperatorio'),
        (3, 'Globalizador'),
        (4, 'Final'),
        (4, 'Otro'),
    ]
    tipo = models.CharField(max_length=60, choices=options)
    Alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT)
    Asignatura = models.ForeignKey(Asignatura, on_delete=models.PROTECT)
    fecha = models.DateField(auto_created=True)
    nota = models.FloatField()
    observacion = models.CharField(max_length=200)
    class meta:
        verbose_name = "Califición"
        verbose_plural_name = "Calificaciones"


# ----------- Situación de revista de los docentes

class Situacion(models.Model):
    options = [
        (1, 'Titular'),
        (2, 'Suplente'),
        (3, 'Provisional')
    ]
    detalle = models.CharField(max_length=60, choices=options)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.PROTECT)
    profesor = models.ForeignKey(Profesor, on_delete=models.PROTECT)
    class meta:
        verbose_name = "Tipo de cargo"
        verbose_plural_name = "Tipos de cargos"
    def __str__(self):
        return self.detalle

