# Generated by Django 3.0.3 on 2020-02-20 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20200217_0952'),
        ('facture', '0003_auto_20200218_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='facture',
            name='client',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.Client'),
        ),
    ]
