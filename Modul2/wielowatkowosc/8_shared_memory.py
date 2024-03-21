'''
Pamięć współdzielona
'''

from multiprocessing import Process, Value, RLock, current_process
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_double
from time import sleep
import logging
import sys

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

def worker(val: Value):
    logger.debug(f'Started {current_process().name}')
    sleep(1)
    with val.get_lock():
        val.value += 1
    logger.debug(f'Done {current_process().name}')
    sys.exit(0)

# if __name__ == '__main__':
#     lock = RLock()
#     value = Value('d', 0, lock=lock)
#     pr1 = Process(target=worker, args=(value, ))
#     pr1.start()
#     pr2 = Process(target=worker, args=(value, ))
#     pr2.start()

#     pr1.join()
#     pr2.join()

#     print(value.value)# 2.0


# Przykład 2

class Point(Structure):
    _fields_ = [('x', c_double), ('y', c_double)]


def modify(num: Value, string: Array, arr: Array):
    logger.debug(f'Started {current_process().name}')
    logger.debug(f"Change num: {num.value}")
    with num.get_lock():
        num.value **= 2
    logger.debug(f"to num: {num.value}")
    with string.get_lock():
        string.value = string.value.upper()
    with arr.get_lock():
        for a in arr:
            a.x **= 2
            a.y **= 2
    logger.debug(f'Done {current_process().name}')


if __name__ == '__main__':
    lock = RLock()
    number = Value(c_double, 1.5, lock=lock)
    string = Array('c', b'hello world', lock=lock)
    array = Array(Point, [(1, -6), (-5, 2), (2, 9)], lock=lock)

    p = Process(target=modify, args=(number, string, array))
    p2 = Process(target=modify, args=(number, string, array))
    p.start()
    p2.start()
    p.join()
    p2.join()
    print(number.value)
    print(string.value)
    print([(arr.x, arr.y) for arr in array])
