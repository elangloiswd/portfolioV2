from django.shortcuts import render
from .models import Work, ProgrammingLanguage, Education, Skill

def index(request):
    Education_object = Education.objects.all().order_by('-start_date')
    Work_objects = Work.objects.all().order_by('created_date')
    Skill_objects = Skill.objects.all().order_by('created_date')

    context = {
        'Education_object': Education_object,
        'Work_object': Work_objects,
        'Skill_object': Skill_objects,
    }
    return render(request, 'home_page/index.html', context)

def work(request):
    Education_object = Education.objects.all().order_by('-start_date')
    Work_objects = Work.objects.all().order_by('-created_date')
    Skill_objects = Skill.objects.all().order_by('created_date')

    context = {'Work_object': Work_objects,
               'Education_object': Education_object,
               'Skill_object': Skill_objects,
               }
    return render(request, 'home_page/work.html', context)

def blog(request):
    return render(request, 'home_page/blog.html')