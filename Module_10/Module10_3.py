from threading import Thread, Lock
import time
import random

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        transactions_limit = 100
        for _ in range(transactions_limit):
            rand_num = random.randint(50, 500)
            self.lock.acquire()
            try:
                self.balance += rand_num
                print(f'Пополнение: {rand_num}. Баланс: {self.balance}')
            finally:
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        transactions_limit = 100
        for _ in range(transactions_limit):
            rand_num = random.randint(50, 500)
            print(f'Запрос на {rand_num}.')
            self.lock.acquire()
            try:
                if rand_num <= self.balance:
                    self.balance -= rand_num
                    print(f'Снятие: {rand_num}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств.')
            finally:
                self.lock.release()
            time.sleep(0.001)

bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
