from django.shortcuts import render
from catalogo.models import Game
from django.core.paginator import Paginator
from django.db.models import Q

def search_games(request):
    query = request.GET.get('q', '')

    results = Game.objects.filter(
        Q(name__icontains=query) | Q(platform__icontains=query)
    ).order_by('id')

    paginator = Paginator(results, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'query': query,
        'list_games' : page_obj,
    }

    return render(request, 'searcher/results_search.html', context)
