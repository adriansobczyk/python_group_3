from setuptools import setup, find_packages

'''
Poradnik jak zbudować własny pakiet oraz jak stworzyć plik setup.py:
https://packaging.python.org/tutorials/packaging-projects/
https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/index.html
'''

setup(
    name='math_operations',
    version='0.1',
    packages=find_packages(), # <-- Odkomentuj tę linię aby pobrać wszystkie pakiety z folderu packages automatycznie
    install_requires = [
        'pandas==2.1.4'
    ],
    # include test files
    package_data={'math_operations': ['tests/*']},
)