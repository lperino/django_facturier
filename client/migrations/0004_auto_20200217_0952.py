# Generated by Django 3.0.3 on 2020-02-17 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_addresses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addresses',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='client.Client'),
        ),
    ]
