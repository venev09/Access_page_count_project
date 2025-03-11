from django.db import models

class AccessCount(models.Model):
    count = models.IntegerField(default=0)
    