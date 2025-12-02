from django.db import models

from pianos.models.piano_category import PianoCategory


class Piano(models.Model):
    model = models.CharField(max_length=150,
                             null=False,
                             blank=False,
                             help_text='Naziv klavira')
    description = models.TextField(max_length=750,
                                   null=True,
                                   blank=True,
                                   help_text='Opis klavira')
    category = models.ForeignKey (PianoCategory,
                                  null=True,
                                  default=0,
                                  on_delete=models.SET_DEFAULT)

    def __str__(self):
        return f'{self.model}  ({self.category.name})'