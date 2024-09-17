from django.shortcuts import render



def main(request):
    return render(request, 'calculator/main.html')


def omlet(request):
    n = int(request.GET.get('servings', 1))
    context = {
        'omlet': {
            'яйца, шт': 2*n,
            'молоко, л': 0.1*n,
            'соль, ч.л.': 0.5*n,
        },
        'person': n,
    }
    return render(request, 'calculator/omlet.html', context)


def pasta(request):
    n = int(request.GET.get('servings', 1))
    context = {
        'pasta': {
            'макароны, г': 0.3*n,
            'сыр, г': 0.05*n,
        },
        'person': n,
    }
    return render(request, 'calculator/pasta.html', context)


def buter(request):
    n = int(request.GET.get('servings', 1))
    context = {
        'buter': {
            'хлеб, ломтик': 1*n,
            'колбаса, ломтик': 1*n,
            'сыр, ломтик': 1*n,
            'помидор, ломтик': 1*n,
        },
        'person': n,
    }
    return render(request, 'calculator/buter.html', context)
