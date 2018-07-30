from django.db import models

class SupportText(models.Model):
    title = models.CharField(max_length=255)
    problem = models.TextField(max_length=2000)
