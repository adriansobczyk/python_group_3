'''
Synchronizacja wątków
'''

from threading import Thread, Condition, Event, Barrier
import logging
from time import sleep, ctime
from random import randint

# Mechanizm Condition (warunek)

def worker(condition: Condition):
    logging.debug('Worker ready to work')
    with condition:
        condition.wait()
        logging.debug('The worker can do the work')

def master(condition: Condition):
    logging.debug('Master doing some work')
    sleep(2)
    with condition:
        logging.debug('Informing that workers can do the work')
        condition.notify_all() # notify(n=1)

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     condition = Condition()
#     master = Thread(name='master', target=master, args=(condition,))

#     worker_one = Thread(name='worker_one', target=worker, args=(condition, ))
#     worker_two = Thread(name='worker_two', target=worker, args=(condition,))
#     worker_one.start()
#     worker_two.start()
#     master.start()

#     logging.debug('End program')



# Mechanizm Event (wydarzenie)

def worker(event: Event):
    logging.debug('Worker ready to work')
    event.wait()
    logging.debug('The worker can do the work')

def master(event: Event):
    logging.debug('Master doing some work')
    sleep(2)
    logging.debug('Informing that workers can do the work')
    event.set()

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     event = Event()
#     master = Thread(name='master', target=master, args=(event, ))

#     worker_one = Thread(name='worker_one', target=worker, args=(event, ))
#     worker_two = Thread(name='worker_two', target=worker, args=(event,))
#     worker_one.start()
#     worker_two.start()
#     master.start()
#     logging.debug('End program')


# Mechanizm Barrier (bariera)
    
def worker(barrier: Barrier):
    logging.debug(f'Start thread: {ctime()}')
    sleep(randint(1, 3))# Simulate some work
    r = barrier.wait()
    logging.debug(f'count: {r}')
    logging.debug(f'Barrier overcome: {ctime()}')

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     barrier = Barrier(6)

#     for num in range(12):
#         thread = Thread(name=f'Th-{num}', target=worker, args=(barrier, ))
#         thread.start()
