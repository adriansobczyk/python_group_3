from mytasks import add

if __name__ == '__main__':
    result = add.delay(1, 5)
    print(result.id)
