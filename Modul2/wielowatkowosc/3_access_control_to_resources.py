'''
Kontrola dostępu do zasobów
'''

from threading import Thread, RLock, Semaphore
import logging
from time import time, sleep


# Lock oraz RLock - blokada wątku

lock = RLock()

def func(locker, delay):
    timer = time()
    locker.acquire()
    sleep(delay)
    locker.release()
    logging.debug(f'Done {time() - timer}')

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     t1 = Thread(target=func, args=(lock, 2))
#     t2 = Thread(target=func, args=(lock, 2))
#     t1.start()
#     t2.start()
#     logging.debug('Started')


# Lock oraz RLock - blokada wątku z wykorzystaniem kontekstu

lock = RLock()

def func(locker, delay):
    timer = time()
    with locker:
        sleep(delay)
    logging.debug(f'Done {time() - timer}')

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     t1 = Thread(target=func, args=(lock, 2))
#     t2 = Thread(target=func, args=(lock, 2))
#     t1.start()
#     t2.start()
#     logging.debug('Started')

# Semafory

def worker(condition):
    with condition:
        logging.debug(f'Got semaphore')
        sleep(1)
        logging.debug(f'finished')

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     pool = Semaphore(5) # oznacza semafor z dwoma dostępnymi zasobami
#     for num in range(10):
#         thread = Thread(name=f'Th-{num}', target=worker, args=(pool, ))
#         thread.start()
