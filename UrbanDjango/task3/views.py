from django.shortcuts import render


# Create your views here.
def main_func(request):
    text = "Главная страница"
    context = {
        'text': text,
    }
    return render(request, "main_page.html", context)


def second_page_func(request):
    main_title = "Игры"
    context = {
        'main_title': main_title,
    }
    return render(request, "second_page.html", context)


def third_page_func(request):
    title = "Извините, ваша корзина пуста"
    context = {
        'title': title,
    }
    return render(request, "third_page.html", context)