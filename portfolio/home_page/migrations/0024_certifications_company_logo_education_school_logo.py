# Generated by Django 5.1.4 on 2025-01-07 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0023_programminglanguage_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='certifications',
            name='company_logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo/'),
        ),
        migrations.AddField(
            model_name='education',
            name='school_logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo/'),
        ),
    ]
