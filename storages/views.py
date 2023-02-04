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
    context = {
        'parts': parts,
    }
    return render(
        request,
        template_name='storages/index.html',
        context=context,
    )
