from django.db import models
# Create your models here.

class Marco(models.Model):
    minx = models.FloatField()
    miny = models.FloatField()
    maxx = models.FloatField()
    maxy = models.FloatField()

class Grupo(models.Model):
    tema = models.CharField(max_length=200)
    objetivos = models.CharField(max_length=600)
    marco = models.ForeignKey(Marco)

EXT_CHOICES = (
    ('V', 'vct'),
    ('R', 'rst'),
    ('G', 'tif'),
)


class Imagenes(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.FileField(max_length=200)
    meta = models.FileField(max_length=200)
    tipo = models.CharField(max_length=1, choices=EXT_CHOICES)

class ImagenesGrupo(models.Model):
    imagen = models.ForeignKey(Imagenes)
    grupo = models.ForeignKey(Grupo)

ROL_USUARIO_CHOICES = (
    ('P','Publicador'),
    ('C','Colaborador'),
)

class Invitaciones(models.Model):
    grupo = models.ForeignKey(Grupo)
    invitado = models.ForeignKey('auth.User')
    anfitrion = models.ForeignKey('auth.User')
    rol = models.CharField(max_length=1, choices=ROL_USUARIO_CHOICES)

class Colaboracion(models.Model):
    grupo = models.ForeignKey(Grupo)
    tema = models.CharField(max_length=100)
    comentario = models.CharField(max_length=200)

class Datos(models.Model):
    colaboracion = models.ForeignKey(Colaboracion)
    x = models.FloatField()
    y = models.FloatField()
    cant = models.FloatField()
    comentario = models.CharField(max_length=100)
    imagen = models.FileField(max_length=200)

BOOLEAN_CHOICES = (
    ('T', 'True'),
    ('F', 'False'),
)

class Publicacion(models.Model):
    grupo = models.ForeignKey(Grupo)
    abstract = models.CharField(max_length=200)
    escrito = models.CharField(max_length=200)
    publicado = models.CharField(max_length=1, choices=BOOLEAN_CHOICES)

class Configuracion(models.Model):
    publ = models.ForeignKey(Publicacion)
    nombre = models.CharField(max_length=100)

class ConfiguracionImagen(models.Model):
    config = models.ForeignKey(Configuracion)
    imagen = models.FileField(max_length=200)
    level = models.IntegerField()
    marco = models.ForeignKey(Marco)

class Usuarios(models.Model):
    grupo = models.ForeignKey(Grupo)
    usuario = models.ForeignKey('auth.User')
    rol = models.CharField(max_length=1, choices=ROL_USUARIO_CHOICES)
