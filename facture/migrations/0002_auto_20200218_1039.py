# Generated by Django 3.0.3 on 2020-02-18 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devis', '0004_auto_20200218_0853'),
        ('facture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facture',
            name='devis',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='devis.Devis'),
        ),
    ]
