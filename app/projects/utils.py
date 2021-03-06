
from django.db.models import Q

from .models import Tag, Project

def searchProjects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(title__icontains=search_query)

    projects = Project.objects.distinct().filter(is_deleted=False).filter(
        Q(title__icontains=search_query) |
        Q(details__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )
    return projects, search_query