from django.db import models


class typeCoffe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
