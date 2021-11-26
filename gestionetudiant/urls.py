"""gestionetudiant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_etudiant import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('ajout_evaluation2/', views.ajout_evaluation2),
    path('ajout_etudiant2/', views.ajout_etudiant2),
    path('ajout_matiere2/', views.ajout_matiere2),
    path('ajout_semestre2/', views.ajout_semestre2),

    path('accueil/', views.accueil),

    path('evaluation/', views.evaluation),
    path('etudiant/', views.etudiant, name='etudiant'),
    path('semestre/', views.semestre),
    path('matiere/', views.matiere),
    path('contact/', views.contact),


#path('modifier/:pk/', views.modifier, name="modifier"),
#path('supprimer/:pk/', views.supprimer, name="supprimer"), /<str:pk>/

    path('modifier/<str:pk>/', views.modifier, name='modifier'),
   # path('supprimer/<int:matricule>',views.supprimer,name='supprimer'),
    path('supprimer/<str:pk>/',views.supprimer,name='supprimer'),

    path('modifier2/<str:pk>/', views.modifier2, name='modifier2'),
    path('supprimer2/<str:pk>/', views.supprimer2, name='supprimer2'),

    path('modifier3/<str:pk>/', views.modifier3, name='modifier3'),
    path('supprimer3/<str:pk>/', views.supprimer3, name='supprimer3'),

    path('modifier4/<str:pk>/', views.modifier4, name='modifier4'),
    path('supprimer4/<str:pk>/', views.supprimer4, name='supprimer4'),
    path('', views.accueil, name='index'),


]
