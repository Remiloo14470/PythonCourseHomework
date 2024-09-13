from threading import Thread
from datetime import datetime
import time

time_start = datetime.now()
def write_words(word_count, file_name):
    counter = 0
    with open(file_name, 'w', encoding='utf-8') as file:
        for word in range(word_count):
            file.write(f'Какое-то слово № {counter+1}\n')
            time.sleep(0.1)
            counter += 1
    print(f'Запись в файл {file_name} завершена')
    return


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(f'Функция cработала за {time_res}')

time_strt = datetime.now()
the_first = Thread(target=write_words, args=(10, 'example5.txt'))
the_second = Thread(target=write_words, args=(30, 'example6.txt'))
the_third = Thread(target=write_words, args=(200, 'example7.txt'))
the_forth = Thread(target=write_words, args=(100, 'example8.txt'))

the_first.start()
the_second.start()
the_third.start()
the_forth.start()

threads = [the_first, the_second, the_third, the_forth]
for t in threads:
    t.join()

time_End = datetime.now()
time_reslt = time_End - time_strt
print(f'Потоки срабоатли за {time_reslt} секунд(ы)')
