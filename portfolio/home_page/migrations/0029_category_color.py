# Generated by Django 5.1.4 on 2025-01-08 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0028_rename_short_post_short_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
