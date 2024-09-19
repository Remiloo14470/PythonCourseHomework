import threading
from queue import Queue
import time
import random


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        rand_num = random.randint(3, 10)
        time.sleep(rand_num)


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for guest in guests:
            table_assigned = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол {table.number}')
                    table_assigned = True
                    break
            if not table_assigned:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables) :
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушел(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if table.guest is None and not self.queue.empty():
                    guest_from_q = self.queue.get()
                    table.guest = guest_from_q
                    guest_from_q.start()
                    print(f'{guest_from_q.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')


if __name__ == "__main__":

    tables = [Table(number) for number in range(1, 6)]
    guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
    guests = [Guest(name) for name in guests_names]
    cafe = Cafe(*tables)
    cafe.guest_arrival(*guests)
    cafe.discuss_guests()