from django.db import models
from django.utils import timezone
# Create your models here.
class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='programming_languages/', blank=True)

    def __str__(self):
        return self.name
    
class Work(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    short_intro = models.CharField(max_length=200, blank=False, null=False)
    programming_languages = models.ManyToManyField(ProgrammingLanguage)
    work_images = models.ImageField(upload_to='work/', blank=True, null=True)
    github_link = models.URLField(("github_link"), max_length=128, db_index=True, unique=False, blank=True)
    website_link = models.URLField(("website_link"), max_length=128, db_index=True, unique=False, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name  # This line defines how a Work object is displayed

class Education(models.Model):
    school = models.CharField(max_length=100, unique=False, blank=False, null=False)
    grade = models.CharField(max_length=200, unique=False, blank=True, null=False)
    program = models.CharField(max_length=200, unique=False, blank=False, null=False)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.school 

class Skill(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    programming_languages = models.ManyToManyField(ProgrammingLanguage)
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name