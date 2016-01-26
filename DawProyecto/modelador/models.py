from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    dueno = models.ForeignKey(User, related_name='proyectos')
    colaboradores = models.ManyToManyField(User, related_name='colaboraciones')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.titulo


class Diagrama(models.Model):
    titulo = models.CharField(max_length=200)
    proyecto = models.ForeignKey(Proyecto, related_name='diagramas')

    def __unicode__(self):
        return self.titulo

# Entidad?

# Atributo?
