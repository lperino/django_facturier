# Generated by Django 3.0.3 on 2020-02-18 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devis', '0003_remove_lignedevis_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lignedevis',
            name='price',
            field=models.IntegerField(),
        ),
    ]