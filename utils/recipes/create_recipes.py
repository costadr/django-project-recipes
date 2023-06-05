from recipes.models import Recipe

from .factory import make_recipe


def new_recipe():
    r = Recipe.objects.get(pk=2)
    new_recipe = make_recipe()

    for i in range(1):
        r.id = None
        r.title = new_recipe['title']
        r.description = new_recipe['description']
        r.slug = new_recipe['slug']
        r.preparation_steps = new_recipe['preparation_steps']
        r.save()

    print("Receitas criadas com sucesso!")

    return r
