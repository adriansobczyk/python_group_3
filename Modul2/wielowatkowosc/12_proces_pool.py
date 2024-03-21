'''
Pula procesów
'''

from multiprocessing import Pool, current_process
import logging
import concurrent.futures
import math

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

def worker(x):
    logger.debug(f"pid={current_process().pid}, x={x}")
    return x*x

if __name__ == '__main__':
    with Pool(processes=2) as pool:
        logger.debug(pool.map(worker, range(10)))


# Pakiet concurrent.futures
PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(4) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
