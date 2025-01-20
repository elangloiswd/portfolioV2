from django.shortcuts import render
from .models import Work, ProgrammingLanguage, Education, Certifications, Skill, Post, Category
from django.shortcuts import get_object_or_404
from random import sample
def home(request):
    Education_object = Education.objects.all().order_by('-start_date')
    Certifications_object = Certifications.objects.all().order_by('-date')
    Work_objects = Work.objects.all().order_by('-created_date')
    Skill_objects = Skill.objects.all().order_by('name')
    Post_objects = Post.objects.all().order_by('created_on')

    context = {
        'Education_object': Education_object,
        'Certifications_object': Certifications_object,
        'Work_object': Work_objects,
        'Skill_object': Skill_objects,
        'Post_object' : Post_objects,
    }
    return render(request, 'home_page/index.html', context)

def work(request):
    Education_object = Education.objects.all().order_by('-start_date')
    Certifications_object = Certifications.objects.all().order_by('-date')
    Work_objects = Work.objects.all().order_by('-created_date')
    Skill_objects = Skill.objects.all().order_by('name')

    context = {'Work_object': Work_objects,
               'Education_object': Education_object,
               'Certifications_object': Certifications_object,
               'Skill_object': Skill_objects,
               }
    return render(request, 'home_page/work.html', context)

def blog(request):
    Education_object = Education.objects.all().order_by('-start_date')
    Certifications_object = Certifications.objects.all().order_by('-date')
    Work_objects = Work.objects.all().order_by('-created_date')
    Skill_objects = Skill.objects.all().order_by('name')
    all_posts = Post.objects.all().order_by('-created_on') 
    all_categories = Category.objects.all().order_by('name') 

    category_name = request.GET.get('category')
    if category_name:
        posts = Post.objects.filter(categories__name=category_name).order_by('-created_on')
        selected_categories = Category.objects.filter(name=category_name)
    else:
        posts = all_posts
        selected_categories = []

    if len(all_posts) < 4:
        random_posts = all_posts
    else:
        random_posts = sample(list(all_posts), 4) 

    context = {
        'Education_object': Education_object,
        'Certifications_object': Certifications_object,
        'Work_object': Work_objects,
        'Skill_object': Skill_objects,
        'Post_object' : posts, 
        'categories': all_categories,
        'selected_categories': selected_categories, 
        'random_posts': random_posts, 
    }
    return render(request, 'home_page/blog.html', context)

def post(request, slug):
    post = get_object_or_404(Post, slug=slug) 
    Post_objects = Post.objects.all().order_by('-created_on') 
    all_posts = Post.objects.all().order_by('-created_on') 
    all_categories = Category.objects.all().order_by('name') 
    # Get all categories
    all_categories = Category.objects.all().order_by('name') 

    # Determine selected categories based on the post's categories
    selected_categories = post.categories.all() 

    if len(all_posts) < 4:
        random_posts = all_posts
    else:
        random_posts = sample(list(all_posts), 4) 

    context = {
        'post': post,
        'Post_object' : Post_objects,
        'categories': all_categories,
        'selected_categories': selected_categories, 
        'random_posts': random_posts, 
    } 
    
    return render(request, 'home_page/post.html', context)