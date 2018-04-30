import os


def size_of():
    with open('text.txt') as f:
        contents = f.read()

    return len(contents)

