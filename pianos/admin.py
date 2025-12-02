from django.contrib import admin

# Register your models here.
from .models.pianos import Piano, PianoCategory, PianoType

admin.site.register