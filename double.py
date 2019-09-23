import threading
import sys


def print_doubling(to_double):
    print(to_double)
    event = threading.Event()
    while not event.wait(1):
        to_double *= 2
        print(to_double)


def get_n():
    try:
        return int(sys.argv[1])
    except:
        return get_input_n()


def get_input_n():
    try:
        return int(input("Enter integer to double: "))
    except:
        return get_input_n()


n = get_n()
print_doubling(n)
