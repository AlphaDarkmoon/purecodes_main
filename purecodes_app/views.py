from django.shortcuts import render
from purecodes_app.models import Post

def home_view(request):
    latest_posts = Post.objects.all().order_by('-created_at')
    return render(request, "purecodes_app/home.html", {'latest_posts': latest_posts})
