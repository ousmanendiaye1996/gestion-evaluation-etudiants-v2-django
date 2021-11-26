from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .formulaire import EtudiantForm, ContactForm, EvaluationForm,MatiereForm,SemestreForm
from .models import Etudiant
from .models import Semestre
from .models import Evaluation
from .models import Matiere
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def accueil(request):

     return render(request, 'accueil.html', {'Etudiant': Etudiant.objects.all()})
     return HttpResponse(template.render())

def evaluation(request):
    return render(request, 'evaluation.html', {'Evaluation': Evaluation.objects.all()})

def semestre(request):
    paginate_by = 2
    return render(request, 'semestre.html', {'Semestre': Semestre.objects.all()})

def matiere(request):
    paginate_by = 3
    return render(request, 'matiere.html', {'Matiere': Matiere.objects.all()})

def etudiant(request):
    return render(request, 'etudiant.html', {'Etudiant': Etudiant.objects.all()})




def ajout_etudiant2(request):
    if request.method == "POST":
        form = EtudiantForm(request.POST).save()
        return redirect('/etudiant')

    else:
        form = EtudiantForm()
        return render(request, 'ajout_etudiant2.html', {'form': form})


def ajout_semestre2(request):
    if request.method == "POST":
        form = SemestreForm(request.POST).save()
        return redirect('/semestre')

    else:
        form = SemestreForm()
        return render(request, 'ajout_semestre2.html', {'form': form})



def ajout_evaluation2(request):
    if request.method == "POST":
        form = EvaluationForm(request.POST).save()
        return redirect('/evaluation')
    else:
        form = EvaluationForm()
        return render(request, 'ajout_evaluation2.html', {'form': form})



       # template = loader.get_template('ajout_evaluation.html')
    # return HttpResponse(template.render())


def ajout_matiere2(request):
    if request.method == "POST":
        form = MatiereForm(request.POST).save()
        return redirect('/matiere')
    else:
        form = MatiereForm()
        return render(request, 'ajout_matiere2.html', {'form': form})




def contact(request):
    if request.method == "POST":
        todoAdd = ContactForm(request.POST)
        if todoAdd.is_valid():
            todoAdd.save()


        return redirect('/contact')

    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})









def modifier(request, pk):
    etudiant = Etudiant.objects.get(matricule=pk)

    form = EtudiantForm(instance=etudiant)

    if request.method == "POST":
        form = EtudiantForm(request.POST, instance = etudiant)
        if form.is_valid():
            form.save()
            messages.success(request, 'cet entree a ete ajoute.')

        return redirect('/etudiant')
    else:
        form = EtudiantForm()
    return render(request, 'ajout_etudiant2.html', {'form': form})


def supprimer(request, pk):
    etudiant = Etudiant.objects.get(matricule = pk)
    etudiant.delete()
    return redirect("/etudiant")



def modifier2(request, pk):
    evaluation = Evaluation.objects.get(idEv=pk)

    form = EvaluationForm(instance=evaluation)

    if request.method == "POST":
        form = EvaluationForm(request.POST, instance = evaluation)
        if form.is_valid():
            form.save()
            messages.success(request, 'cet entree a ete ajoute.')

        return redirect('/evaluation')
    else:
        form = EvaluationForm()
    return render(request, 'ajout_evaluation2.html', {'form': form})


def supprimer2(request, pk):
    evaluation = Evaluation.objects.get(idEv = pk)
    evaluation.delete()
    return redirect("/evaluation")







def modifier3(request, pk):
    matiere = Matiere.objects.get(idMatiere=pk)

    form = MatiereForm(instance=matiere)

    if request.method == "POST":
        form = MatiereForm(request.POST, instance = matiere)
        if form.is_valid():
            form.save()
            messages.success(request, 'cet entree a ete ajoute.')

        return redirect('/matiere')
    else:
        form = MatiereForm()
    return render(request, 'ajout_matiere2.html', {'form': form})


def supprimer3(request, pk):
    matiere = Matiere.objects.get(idMatiere = pk)
    matiere.delete()
    return redirect("/matiere")






def modifier4(request, pk):
    semestre = Semestre.objects.get(idSemestre=pk)

    form = SemestreForm(instance=semestre)

    if request.method == "POST":
        form = SemestreForm(request.POST, instance = semestre)
        if form.is_valid():
            form.save()
            messages.success(request, 'cet entree a ete ajoute.')

        return redirect('/semestre')
    else:
        form = SemestreForm()
    return render(request, 'ajout_semestre2.html', {'form': form})


def supprimer4(request, pk):
    semestre = Semestre.objects.get(idSemestre = pk)
    semestre.delete()
    return redirect("/semestre")










