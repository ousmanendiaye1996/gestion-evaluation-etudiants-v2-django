# Generated by Django 3.2.8 on 2021-10-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_etudiant', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=2055),
        ),
    ]
