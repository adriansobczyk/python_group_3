'''
Tworzenie wątków
'''

from threading import Thread, Timer
import logging
from time import sleep

# Wątek jako klasa
class MyThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self) -> None:
        sleep(2)
        logging.debug('Wake up!')
        logging.debug(f"args: {self.args}")

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     for i in range(3):
#         thread = MyThread(args=(f"Count thread - {i}",))
#         thread.start()
#     print('Useful message')

# Wątek jako funktor

class UsefulClass():
    def __init__(self, second_num):
        self.delay = second_num

    def __call__(self):
        sleep(self.delay)
        logging.debug('Wake up!')

# if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    # t2 = UsefulClass(2)
    # t3 = UsefulClass(3)
    # thread = Thread(target=t2)
    # thread_two = Thread(target=t3)
    # thread.start()
    # thread_two.start()

    # print('Some stuff')


# Wątek jako funkcja
    
def example_work(delay):
    sleep(delay)
    logging.debug('Wake up!')

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     for i in range(5):
#         thread = Thread(target=example_work, args=(i,))
#         thread.start()


# Metoda join - czekanie na zakończenie wątków

def example_work(params):
    sleep(params)
    logging.debug('Wake up!')

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     logging.debug('Start program')
#     threads = []
#     for i in range(5):
#         thread = Thread(target=example_work, args=(i,))
#         thread.start()
#         threads.append(thread)

#     [el.join() for el in threads]

#     logging.debug('End program')


# Metoda is_alive - sprawdzenie czy wątek nadal działa

class UsefulClass:
    def __init__(self, second_num):
        self.delay = second_num

    def __call__(self):
        sleep(self.delay)
        logging.debug('Wake up!')

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     t2 = UsefulClass(2)
#     thread = Thread(target=t2)
#     thread_locking = Thread(target=t2)

#     thread.start()
#     print(thread.is_alive(), thread_locking.is_alive())
#     thread_locking.start()
#     thread.join()
#     thread_locking.join()
#     print(thread.is_alive(), thread_locking.is_alive())
#     print('After all...')


# Wątki timer - wywołanie funkcji po określonym czasie

def example_work():
    logging.debug('Start!')

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

#     first = Timer(0.5, example_work)
#     first.name = 'First thread'
#     second = Timer(0.7, example_work)
#     second.name = 'Second thread'
#     logging.debug('Start timers')
#     first.start()
#     second.start()
#     sleep(0.6)
#     second.cancel()

#     logging.debug('End program')
