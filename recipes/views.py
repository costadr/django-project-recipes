from django.shortcuts import get_list_or_404, render

from utils.recipes.factory import make_recipe

from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,  # category é uma foreing key que tem um id
            is_published=True
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | '
    })


def about(request):
    return render(request, 'recipes/pages/about.html', context={'name': 'Diogo'})


def contact(request):
    return render(request, 'recipes/pages/contact.html')


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
