from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from utils.pagination import make_pagination

from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, 9)

    return render(request, 'recipes/pages/home.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,  # category é uma foreing key que tem um id
            is_published=True
        ).order_by('-id')
    )

    page_obj, pagination_range = make_pagination(request, recipes, 9)

    return render(request, 'recipes/pages/category.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'title': f'{recipes[0].category.name} - Category | '
    })


def about(request):
    return render(request, 'recipes/pages/about.html', context={'name': 'Diogo'})


def contact(request):
    return render(request, 'recipes/pages/contact.html')


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |  # o i ignora o fato de ser maiúscula ou minúscula
            Q(description__icontains=search_term),  # o pipe | significa OU
        ),
        is_published=True,
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, 9)

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}"',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}',
    })
