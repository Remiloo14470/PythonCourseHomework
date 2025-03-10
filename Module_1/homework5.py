immutable_var = 134, 'my name is', True, 16.5
print(immutable_var)
#immutable_var [0] = 155
#print(immutable_var) # кортеж не поддерживает обращение по элементам
mutable_list = [134, 'my name is', True, 16.5]
mutable_list[2] = False
print(mutable_list)
