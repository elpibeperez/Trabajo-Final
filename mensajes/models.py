from django.db import models

BOOLEAN_CHOICES = (
    ('T', 'True'),
    ('F', 'False'),
)


class Mensaje(models.Model):
    rte = models.ForeignKey('auth.User', related_name="remitente")
    mens = models.CharField(max_length=800)
    leido = models.CharField(max_length=1, choices=BOOLEAN_CHOICES)

    def __unicode__(self):
        return self.mens

class Sistema_Mensaje(models.Model):
    mensaje = models.ForeignKey(Mensaje)
    destino = models.ForeignKey('auth.User')

    def __unicode__(self):
        return self.mensaje.__unicode__()
# Create your models here.
