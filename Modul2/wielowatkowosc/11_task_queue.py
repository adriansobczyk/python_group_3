'''
Kolejka zadań
'''

from multiprocessing import JoinableQueue, Process, current_process, Queue
from time import sleep
import sys
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

# Przykład 1

q = Queue()

def worker(queue: Queue):
    name = current_process().name
    logger.debug(f'{name} started...')
    val = queue.get()
    logger.debug(f'{name} {val**2}')
    sys.exit(0)

if __name__ == '__main__':
    w1 = Process(target=worker, args=(q, ))
    w2 = Process(target=worker, args=(q, ))

    w1.start()
    w2.start()

    q.put(8)
    sleep(1)
    q.put(16)


# Przykład 2

# jq = JoinableQueue()

# def worker(jqueue: JoinableQueue):
#     name = current_process().name
#     logger.debug(f'{name} started...')
#     val = jqueue.get()
#     logger.debug(f'{name} {val**2}')
#     sleep(1)
#     jqueue.task_done()
#     sys.exit(0)

# if __name__ == '__main__':
#     w1 = Process(target=worker, args=(jq, ))
#     w2 = Process(target=worker, args=(jq, ))

#     w1.start()
#     w2.start()

#     jq.put(8)
#     sleep(1)
#     jq.put(16)
#     jq.join()
#     print('Finished')
