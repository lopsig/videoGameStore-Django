from django.shortcuts import render
from django.core.paginator import Paginator
from catalogo.models import Game

def list_games(request):
    games = Game.objects.all().order_by('id')
    paginator = Paginator(games, 3)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context_catalog_games = {'list_games': page_obj}
    return render(request, 'catalogo/list_games.html',
                  context_catalog_games)
