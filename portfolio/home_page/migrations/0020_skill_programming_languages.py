# Generated by Django 5.1.1 on 2024-10-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0019_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='programming_languages',
            field=models.ManyToManyField(to='home_page.programminglanguage'),
        ),
    ]
