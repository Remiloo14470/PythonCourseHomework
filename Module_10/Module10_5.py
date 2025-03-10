import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print('Многопроцессный', end - start)

    start_time = datetime.datetime.now()
    for file in filenames:
        read_info(file)
    end_time = datetime.datetime.now()
    print('Линейный', end_time - start_time)
