from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
# Create your views here.
def posts_list(request):
    # n = ['Oleg', 'Masha', 'Olga', 'Ksu']
    # return render(request, 'blog/index.html', context={'names': n})
   
    posts = Post.objects.all()
    # print(posts, "-----------------------")
    return render(request, 'blog/index.html', context={'posts': posts})














