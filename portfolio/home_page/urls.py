from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import blog, post, home

urlpatterns = [
    path('home/', views.home, name='home'),
    path('work/', views.work, name='work'),
    path('blog/', views.blog, name='blog'),
    path('<slug:slug>/', views.post, name='post'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)