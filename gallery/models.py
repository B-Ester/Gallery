from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    name = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False, width_field="width", height_field="height")
    timestamp = models.DateTimeField(blank=False, auto_now=1, auto_now_add=0)
    likes = models.IntegerField(blank=True, default=0)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]

