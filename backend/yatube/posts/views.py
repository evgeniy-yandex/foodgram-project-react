# posts/views.py

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
#    return HttpResponse('Главная страница')
    return render(request, 'posts/index.html')

def group_posts(request, post_slug): # Переменная post_slug из posts/urls.py
#    return HttpResponse(f'Cтраница {post_slug} для постов, '
#                         'отфильтрованных по группам')
    return render(request, 'posts/group_list.html')
