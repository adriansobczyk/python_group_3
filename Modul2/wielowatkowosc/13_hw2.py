import multiprocessing


def square(number):
    return number ** 2

def square_async(numbers):
    num_processes = multiprocessing.cpu_count()
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(square, numbers)
    return results

if __name__ == '__main__':
    # Synchronous execution
    print("Synchronous execution")
    a = square(128)
    print(a)
    b = square(255)
    print(b)
    c = square(1024)
    print(c)
    d = square(5176)
    print(d)

    # Asynchronous execution
    print("Asynchronous execution")
    a, b, c, d = square_async([128, 255, 1024, 5176])
    print(a)
    print(b)
    print(c)
    print(d)