# Generated by Django 2.2 on 2021-09-17 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VitalData', '0003_physicalvital'),
    ]

    operations = [
        migrations.AddField(
            model_name='biotag',
            name='hip_circum',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='biotag',
            name='waist_cicrum',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='biotag',
            name='whr_ratio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='physicalvital',
        ),
    ]
