from django.db import models
from django.contrib import admin


class Etudiant(models.Model):
    matricule = models.BigAutoField(primary_key=True, unique=True)
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=20)
    classe = models.CharField(max_length=30)
    sexe = models.CharField(max_length=30)
    nationalite= models.CharField(max_length=25)
    moyenne= models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.nom, self.prenom)



class Semestre(models.Model):
    idSemestre = models.BigAutoField(primary_key=True, unique=True)
    nomSemestre = models.CharField(max_length=30)

    def __str__(self):
        return self.nomSemestre

class Evaluation(models.Model):
    idEv = models.BigAutoField(primary_key=True, unique=True)
    nomEvaluation = models.CharField(max_length=100)
    typeEvaluation = models.CharField(max_length=100)
    dateEvaluation = models.DateField()
    idSemestreEvaluation = models.ForeignKey(Semestre, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomEvaluation

class Matiere(models.Model):
    idMatiere = models.BigAutoField(primary_key=True, unique=True)
    nomMatiere = models.CharField(max_length=30)
    sommeHoraire = models.CharField(max_length=30)
    nbcredit = models.IntegerField()
    matricule = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    idEv = models.ForeignKey(Evaluation, on_delete=models.CASCADE)


# etudiant = models.ManyToManyField(Etudiant)


class Contact(models.Model):
    nomComplet = models.CharField(max_length=100)
    email = models.EmailField(max_length=75)
    sujet = models.CharField(max_length=100)
    message = models.CharField(max_length=2055)


class Contact_Admin(admin.ModelAdmin):
    ordering = ('nomComplet',)
    list_display = ('nomComplet', 'email', 'sujet', 'message',)
    list_filter = ('id',)
    search_fields = ('id', 'nomComplet')

class Semestre_Admin(admin.ModelAdmin):
        # afficher les etudiants qui ont dans la bd
        list_display = ('idSemestre', 'nomSemestre')
        # creer un champs de recherch
        list_filter = ('idSemestre',)
        search_fields = ('idSemestre', 'nomSemestre')
        ordering = ('idSemestre',)


class Evaluation_Admin(admin.ModelAdmin):
            # afficher les etudiants qui ont dans la bd
            list_display = ('nomEvaluation', 'typeEvaluation', 'dateEvaluation', 'idSemestreEvaluation')
            # creer un champs de recherch
            ordering = ('idEv',)
            list_filter = ('idEv',)
            # creer un champs de recherch
            search_fields = ('idEv', 'nomEvaluation')
class Matiere_Admin(admin.ModelAdmin):
    ordering = ('idMatiere',)
    list_display = ('idMatiere', 'nomMatiere', 'sommeHoraire', 'nbcredit','matricule','idEv')
    list_filter = ('idMatiere',)
    search_fields = ('idMatiere', 'nomMatiere')

admin.site.register(Matiere, Matiere_Admin)

admin.site.register(Evaluation, Evaluation_Admin)

admin.site.register(Semestre, Semestre_Admin)

admin.site.register(Contact, Contact_Admin)

# Class qui permet d'afficher la liste de etudiant dans la page admin et la bare de recherche par code produit
class EtudiantAdmin(admin.ModelAdmin):
    # afficher les etudiants qui ont dans la bd
    list_display = ('matricule', 'nom', 'prenom', 'classe', 'sexe', 'nationalite','moyenne')
    #creer un champs de recherch
    list_filter = ('matricule',)
    # creer un champs de recherch
    search_fields = ('matricule', 'nom')

    class EvaluationAdmin(admin.ModelAdmin):
        # afficher les etudiants qui ont dans la bd
        list_display = ('nomEvaluation', 'typeEvaluation', 'dateEvaluation', 'idSemestreEvaluation')
        # creer un champs de recherch
        list_filter = ('idEv',)
        # creer un champs de recherch
        search_fields = ('idEv', 'nomEvaluation')



