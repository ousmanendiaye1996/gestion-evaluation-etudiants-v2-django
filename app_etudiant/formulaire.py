from django.forms import ModelForm
from .models import Etudiant, Evaluation, Contact, Matiere, Semestre


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['nomComplet', 'email', 'sujet', 'message']

class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = ['matricule', 'nom', 'prenom', 'classe', 'sexe', 'nationalite','moyenne']
class SemestreForm(ModelForm):
    class Meta:
        model = Semestre
        fields = ['nomSemestre']

class MatiereForm(ModelForm):
    class Meta:
        model = Matiere
        fields = ['nomMatiere', 'sommeHoraire', 'nbcredit','matricule','idEv']


class EvaluationForm(ModelForm):
            # classe meta c une classe qui utilise une classe il va indiquer a django quel model qui va utiliser pour creer le formulaire
            class Meta:
                # les champs qui vont s'afficher dans le formulaire d'insertion
                model = Evaluation
                fields = ['nomEvaluation', 'typeEvaluation', 'dateEvaluation', 'idSemestreEvaluation']

                def modifier(request, pk):
                    etudiant = Etudiant.objects.get(id=pk)

                    form = EtudiantForm(instance=etudiant)

                    if request.method == "POST":
                        form = EtudiantForm(request.POST, instance=etudiant).save()

                        return redirect("/liste")

                    return render(request, "ajout_etudiant.html", {"form": form})

                def supprimer(request, pk):
                    etudiant = Etudiant.objects.get(id=pk)
                    etudiant.delete()
                    return redirect("/liste")