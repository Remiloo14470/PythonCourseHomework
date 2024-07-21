# 1
def print_params(a=1, b='строка', c=8):
    print(a, b, c)


print_params(a=3, b=5)
print_params()
print_params(b=25)
print_params(c=[1,2,3])

# 2
values_list = [5, 'animal', False]
values_dict = {'a': 8, 'b': True, 'c': 'baby'}

print_params(*values_list)
print_params(**values_dict)

# 3
values_list_2 = [True, 314.20]
print_params(*values_list_2, 42)