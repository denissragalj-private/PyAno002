from django.contrib import admin

from .models.chords import Chord, ChordCategory, ChordType

# Register your models here.
admin.site.register([Chord, ChordCategory, ChordType])
