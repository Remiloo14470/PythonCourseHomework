first_strings = ['Elon', 'Mask', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [x for x in first_strings if len(x)>5]
second_result = [(x,y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {x: len(x) for x in (first_strings + second_strings) if len(x) % 2 == 0}
print(third_result)
