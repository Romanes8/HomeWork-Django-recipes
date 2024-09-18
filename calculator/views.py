from django.shortcuts import render
from calculator.data import DATA


#функция отображения главной страницы со списком рецептов
def main(request):
    context = {
        'DATA': DATA
    }
    return render(request, 'calculator/main.html', context)


#функция отображения рецептов
def recipe(request, recipe_str):
    n = int(request.GET.get('servings', 1)) #запрос на получение количества персон
    ingredients = DATA.get(recipe_str) #получение словаря ингредиентов из DATA по ключу recipe_str (recipe_str - переменная динамического url)
    servings_ingredients = {} #получение словаря с количеством ингредиентов, умноженным на количество персон.
    for el in ingredients.items():
        servings_ingredients[el[0]] = el[1]*n
    context = {
        'recipe_str': recipe_str,
        'ingredients': servings_ingredients,
        'person': n,
    }
    return render(request, 'calculator/index.html', context)
