from django.contrib.postgres.fields import JSONField
from django.db import models


class Track(models.Model):
    points = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
