# Generated by Django 4.1.1 on 2022-10-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_models',
            name='setor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stock_models',
            name='sub_setor',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
