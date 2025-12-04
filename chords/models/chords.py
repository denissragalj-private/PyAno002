from django.db import models

from .chord_category import ChordCategory
from .chord_type import ChordType


class Chord(models.Model):
    model = models.CharField(max_length=150,
                             null=False,
                             blank=False,
                             help_text='Naziv Akorda')
    description = models.TextField(max_length=750,
                                   null=True,
                                   blank=True,
                                   help_text='Opis klavira')

    category = models.ForeignKey(ChordCategory,
                                 null=False,
                                 default=0,
                                 on_delete=models.SET_DEFAULT)

    type = models.ForeignKey(ChordType,
                             null=False,
                             default=0,
                             on_delete=models.SET_DEFAULT)

    picture_url = models.CharField(max_length=750,
                                   null=True,
                                   blank=True,
                                   help_text='Upisite link do slike akorda')

    def __str__(self):
        return f'{self.model} ({self.category.name})'
