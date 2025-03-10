import io
def custom_write(file_name, strings):
    string_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for line_num, line in enumerate(strings, start=1):
            start = file.tell()
            file.write(f'{line} \n')
            string_positions[(line_num, start)] = line
    return string_positions

info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)


