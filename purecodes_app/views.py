from django.shortcuts import render
from purecodes_app.models import Post

from django.db.models import Q

def home_view(request):
    query = request.GET.get('q','')  # Get the search query from the URL parameter 'q'
    latest_posts = Post.objects.all().order_by('-created_at')

    if query:
        # If a search query is provided, filter the posts by title containing the query
        latest_posts = latest_posts.filter(title__icontains=query)

    elif query == 'None':
        query = ''

    return render(request, "purecodes_app/home.html", {'latest_posts': latest_posts, 'query': query})

