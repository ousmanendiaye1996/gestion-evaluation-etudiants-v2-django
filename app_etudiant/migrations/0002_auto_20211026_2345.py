# Generated by Django 3.2.8 on 2021-10-26 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_etudiant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('idEv', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('nomEvaluation', models.CharField(max_length=100)),
                ('typeEvaluation', models.CharField(max_length=100)),
                ('dateEvaluation', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('idSemestre', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('nomSemestre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('idMatiere', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('nomMatiere', models.CharField(max_length=30)),
                ('sommeHoraire', models.CharField(max_length=30)),
                ('nbcredit', models.IntegerField()),
                ('idEv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_etudiant.evaluation')),
                ('matricule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_etudiant.etudiant')),
            ],
        ),
        migrations.AddField(
            model_name='evaluation',
            name='idSemestreEvaluation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_etudiant.semestre'),
        ),
    ]
