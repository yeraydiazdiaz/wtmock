import os
from helper import Helper


def work_on():
    path = os.getcwd()
    print(f'Working on {path}')
    return path
