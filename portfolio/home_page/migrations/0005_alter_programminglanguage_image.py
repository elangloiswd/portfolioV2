# Generated by Django 5.1.1 on 2024-10-03 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0004_alter_programminglanguage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programminglanguage',
            name='image',
            field=models.ImageField(blank=True, upload_to='../static/assets/images/programming_languages/'),
        ),
    ]
