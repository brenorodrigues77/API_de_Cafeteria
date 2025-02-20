from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from companyCoffe.models import companyCoffe


class reviewCoffe(models.Model):
    companycoffe = models.ForeignKey(
        companyCoffe, on_delete=models.PROTECT, related_name='review')
    stars = models.IntegerField(validators=[
        MinValueValidator(
            0, 'Sua avaliação nao pode ser menor que 0 estrelas.'),
        MaxValueValidator(
            5, 'Sua avaliação nao pode ser maior que 5 estrelas.'),
    ])
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.companycoffe)
