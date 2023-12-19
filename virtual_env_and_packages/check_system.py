import platform


def check_if_windows():
    if platform.system() == 'Windows':
        print('Windows')
    else:
        print('Not Windows')


def check_if_linux():
    if platform.system() == 'Linux':
        print('Linux')
    else:
        print('Not Linux')


def check_if_mac():
    if platform.system() == 'Darwin':
        print('Mac')
    else:
        print('Not Mac')


def check_system():
    print('Checking system...')
    print('System: ' + platform.system())
    print('Version: ' + platform.version())
    print('Release: ' + platform.release())
    print('Machine: ' + platform.machine())
    print('Processor: ' + platform.processor())
    print('Architecture: ' + platform.architecture()[0])
    print('Python version: ' + platform.python_version())
    print('Python implementation: ' + platform.python_implementation())
    print('Python compiler: ' + platform.python_compiler())


# if __name__ == '__main__':
    # check_if_windows()
    # check_if_linux()
    # check_if_mac()
    # check_system()