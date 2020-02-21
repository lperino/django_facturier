# Generated by Django 3.0.3 on 2020-02-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0002_auto_20200218_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='lignefacture',
            name='description',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lignefacture',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lignefacture',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]