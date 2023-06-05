# from inspect import signature
import random

from django.utils.text import slugify
from faker import Faker


def rand_ratio():
    return random.randint(840, 900), random.randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_recipe():
    mytitle = fake.sentence(nb_words=6)

    return {
        # 'id': None,  # fake.random_number(digits=2, fix_len=True),
        'title': mytitle,
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': random.choice(["Carnes", "Café da manhã", "Vegana"])  # fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        },
        'slug': slugify(mytitle),
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())
