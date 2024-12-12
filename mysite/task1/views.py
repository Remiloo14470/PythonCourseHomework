from django.shortcuts import render
from .models import Buyer, Game


def main(request):
    page_title = "Главная страница"
    context = {
        'page_title': page_title,
    }
    return render(request, "main_page.html", context)


def games(request):
    page_title = "Игры"
    list_of_games = Game.objects.all()
    context = {
        'page_title': page_title,
        'list_of_games': list_of_games
    }
    return render(request, "second_page.html", context)


def cart(request):
    page_title = "Корзина"
    text = "Извините, ваша корзина пуста"
    context = {
        'page_title': page_title,
        'text': text
    }
    return render(request, "third_page.html", context)


from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        info['form'] = form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration.html', context=info)
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration.html', context=info)
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration.html', context=info)
            Buyer.objects.create(name=username, balance=0, age=age)
            return HttpResponse(f'Добро пожаловать, {username}!')
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'registration.html', context=info)
