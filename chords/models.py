from django.db import models

# Create your models here.
class Chord(models.Model):
    model = models.CharField(max_length=150, 
                             null=False,
                             blank=False,
                             help_text='Naziv Akorda')
    description = models.TextField(max_length=750,
                                   null=True,
                                   blank=True,
                                   help_text='Opis akorda')

class ChordType(models.Model):
    name = models.CharField(max_length=150, 
                             null=False,
                             blank=False,
                             help_text='Naziv akorda')