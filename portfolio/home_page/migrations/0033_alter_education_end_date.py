# Generated by Django 5.1.4 on 2025-01-10 21:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0032_alter_education_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
