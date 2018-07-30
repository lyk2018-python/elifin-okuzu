from django.db import models

class Issue(models.Model):
    title = models.CharField(max_length=255)
    explantation = models.TextField(max_length=2000)
