from django.shortcuts import render


# Create your views here.
def main_func(request):
    page_title = "Главная страница"
    context = {
        'page_title': page_title,
    }
    return render(request, "main_page.html", context)


def second_page_func(request):
    page_title = "Игры"
    list_of_games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay2']
    context = {
        'page_title': page_title,
        'list_of_games': list_of_games
    }
    return render(request, "second_page.html", context)


def third_page_func(request):
    page_title = "Корзина"
    text = "Извините, ваша корзина пуста"
    context = {
        'page_title': page_title,
        'text': text
    }
    return render(request, "third_page.html", context)