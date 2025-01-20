from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
from django.template.defaultfilters import slugify 
# Create your models here.
class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=100, blank=True)
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
        return self.name

class Education(models.Model):
    school = models.CharField(max_length=100, unique=False, blank=False, null=False)
    grade = models.CharField(max_length=200, unique=False, blank=True, null=False)
    program = models.CharField(max_length=200, unique=False, blank=False, null=False)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now, blank=True, null=True)
    school_logo = models.ImageField(upload_to='logo/', blank=True, null=True)

    def __str__(self):
        return self.school 
class Certifications(models.Model):
    name = models.CharField(max_length=100, unique=False, blank=False, null=False)
    company = models.CharField(max_length=200, unique=False, blank=True, null=False)
    date = models.DateField(default=timezone.now)
    company_logo = models.ImageField(upload_to='logo/', blank=True, null=True)

    def __str__(self):
        return self.name
class Skill(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    icon = models.CharField(max_length=100, blank=False, null=True)
    programming_languages = models.ManyToManyField(ProgrammingLanguage)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
#BLOG
class Category(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    short = models.CharField(max_length=255, blank=False, null=True)
    body = CKEditor5Field('Text', config_name='extends')
    img = models.ImageField(upload_to='blog/', blank=True, null=True)
    created_on = models.DateField(default=timezone.now)
    last_modified = models.DateField(default=timezone.now)
    categories = models.ManyToManyField("Category", related_name="posts")
    author = models.CharField(max_length=60)
    slug = models.SlugField(max_length=255, unique=True, blank=True) 
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs) 