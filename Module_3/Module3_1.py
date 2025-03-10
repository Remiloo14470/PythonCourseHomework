calls = 0


def count_calls():  # подсчитывает вызовы других функций
    global calls
    calls += 1


def string_info(string):
    count_calls()
    length = len(string)
    reg1 = string.upper()
    reg2 = string.lower()
    tuple = length, reg1, reg2
    return tuple


def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    list_to_search_lower = [item.lower() for item in list_to_search]

    if string_lower in list_to_search_lower:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
