# Generated by Django 4.1.1 on 2022-09-07 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instituicao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instituicaomodel',
            name='cnpj',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='instituicaomodel',
            name='nome',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instituicaomodel',
            name='pais',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
