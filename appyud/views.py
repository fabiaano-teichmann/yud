from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.
def listar_post(request):
    posts = Post.objects.all()

    return render(request, 'appyud/listar_post.html', {'posts': posts})
