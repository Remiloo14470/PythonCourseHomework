from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
def sign_up_by_django(request):
    users = ['Alex', 'Tom', 'Kate', 'Debbie', 'Spencer']
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        info['form'] = form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username not in users:
                if password == repeat_password:
                    if int(age) >= 18:
                        return HttpResponse(f"Приветствуем тебя, {username}!")
                    else:
                        info['error'] = 'Вы должны быть старше 18'
                        return render(request, 'fifth_task/registration_page.html', context=info)
                else:
                    info['error'] = 'Пароли не совпадают'
                    return render(request, 'fifth_task/registration_page.html', context=info)
            else:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'fifth_task/registration_page.html', context=info)
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_html(request):
    users = ['Alex', 'Tom', 'Kate', 'Debbie', 'Spencer']
    info = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username not in users:
            if password == repeat_password:
                if int(age) >= 18:
                    return HttpResponse(f"Приветствуем тебя, {username}!")
                else:
                    info['error'] = 'Вы должны быть старше 18'
                    return render(request, 'fifth_task/registration_page.html', context=info)
            else:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'fifth_task/registration_page.html', context=info)
        else:
            info['error'] = 'Пользователь уже существует'
            return render(request, 'fifth_task/registration_page.html', context=info)
    return render(request, 'fifth_task/registration_page.html', context=info)
