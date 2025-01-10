from django.db import models
from typeCoffe.models import typeCoffe
from descriptionCoffe.models import descriptionCoffe

class companyCoffe(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    typecoffe = models.ForeignKey(typeCoffe, on_delete=models.PROTECT, related_name='choices')
    release_date = models.DateField(blank=True, null=True)
    descriptioncoffe = models.ManyToManyField(descriptionCoffe, related_name='choices')
    resume = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    