# Generated by Django 5.1.1 on 2024-10-04 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0014_education'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='created_date',
            new_name='date',
        ),
    ]
