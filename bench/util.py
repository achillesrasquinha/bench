from collections import MutableSequence

def sequencify(arg):
    if not isinstance(arg, MutableSequence):
        arg = [arg]
    return arg

def assign_if_empty(a, b):
    if not a:
        a = b
    return a