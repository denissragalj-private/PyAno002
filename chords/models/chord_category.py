from django.db import models


class ChordCategory(models.Model):
    name = models.CharField(max_length=150,
                             null=False,
                             blank=False,
                             help_text='Kategorija Akorda')

    def __str__(self):
        return f'{self.name}'
