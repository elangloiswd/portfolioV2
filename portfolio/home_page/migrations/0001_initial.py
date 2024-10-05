# Generated by Django 5.1.1 on 2024-10-03 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_intro', models.CharField(max_length=200)),
                ('work_images', models.ImageField(blank=True, null=True, upload_to='')),
                ('github_link', models.URLField(blank=True, db_index=True, max_length=128, verbose_name='github_link')),
                ('website_link', models.URLField(blank=True, db_index=True, max_length=128, verbose_name='website_link')),
                ('programming_languages', models.ManyToManyField(to='home_page.programminglanguage')),
            ],
        ),
    ]
