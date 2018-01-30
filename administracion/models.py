# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from django.utils import timezone

# Create your models here.
class Suministros_tipos(models.Model):
	descripcion = models.CharField(max_length=100)	


class Suministros(models.Model):
	descripcion = models.CharField(max_length=100)
	tipo = models.ForeignKey(Suministros_tipos, null=True)
	valor_referencial  = models.IntegerField(default=0)
	
 