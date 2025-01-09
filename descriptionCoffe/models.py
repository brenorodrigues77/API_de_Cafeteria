from django.db import models

NATIONALITY_CHOICE = (
    ('BRA', 'Brazil'),
    ('IT', 'Italy'),
)

class descriptionCoffe(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    creation_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICE, blank=True, null=True)

    def __str__(self):
        return self.name
    
