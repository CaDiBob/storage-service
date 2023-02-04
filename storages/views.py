from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q

from .models import Part


def index(request):
    parts = Part.objects.all()
    query = request.GET.get('search')
    if query:
        parts = parts.filter(
            Q(name__icontains=query) | Q(code__icontains=query)
        )
    paginator = Paginator(parts, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(
        request,
        template_name='storages/index.html',
        context=context,
    )
