# Generated by Django 4.2.17 on 2025-01-06 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0020_skill_programming_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='icon',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
