from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about),
    path('contact/', views.contact),
    path('recipes/<int:id>/', views.recipe, name="recipe"),

    path('recipes/category/<int:category_id>/', views.category, name="category"),
]
