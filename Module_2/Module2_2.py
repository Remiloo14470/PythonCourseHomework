first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second == third:
     print('Результат: 3')
elif first == second or first == third or second == third:
    print('Результат: 2')
elif first != second and first != third and second != third:
    print('Результат: 0')
