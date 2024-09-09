def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        if number <= 1:
            print(' Составное')
        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                print(f'Составное')
            else:
                print('Простое')
            return number
    return wrapper


@is_prime
def sum_three(*args):
    result = sum(args)
    return result


result = sum_three(2, 3, 6)
print(result)