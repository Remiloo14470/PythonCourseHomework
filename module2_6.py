import random

numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
stone1 = random.choice(numbers)

result = ''
for j in range(1, stone1):
    for k in range(j+1, stone1):
        if stone1 % (j + k) == 0:
            result += str(j) + str(k)
print(f'Случайное число: {stone1}')
print(f'Пароль: {result}')