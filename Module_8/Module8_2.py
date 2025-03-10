def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            print(f'Некорректный тип данных для подсчета суммы - {i}')
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        num = 0
        for i in numbers:
            if isinstance(i, int):
                num += 1
        tuple = personal_sum(numbers)
        result_1 = tuple[0] / num
        return result_1
    except ZeroDivisionError as exc:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
