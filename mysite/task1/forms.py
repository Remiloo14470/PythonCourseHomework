from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Ваш логин')
    password = forms.CharField(max_length=8, label='Ваш пароль')
    repeat_password = forms.CharField(max_length=8, label='Повторите пароль')
    age = forms.IntegerField(label='Ваш возраст')