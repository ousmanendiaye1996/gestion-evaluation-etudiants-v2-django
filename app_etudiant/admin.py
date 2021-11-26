from django.contrib import admin
from .models import Etudiant, EtudiantAdmin
from .models import Evaluation
from .models import Semestre
from .models import Matiere

# Register your models here.
admin.site.register(Etudiant, EtudiantAdmin)

