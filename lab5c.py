#!/usr/bin/env python3

# Author ID: Ssamadivaghefi



def add(number1, number2):

    """Add two numbers together, or return error string if not possible."""

    try:

        a = int(number1)

        b = int(number2)

        return a + b

    except (TypeError, ValueError):

        return 'error: could not add numbers'



def read_file(filename):

    """Read a file and return its list of lines, or error string if file not found."""

    try:

        with open(filename, 'r') as f:

            return f.readlines()

    except OSError:

        return 'error: could not read file'



if __name__ == '__main__':

    print(add(10,5))                # works

    print(add('10',5))              # works

    print(add('abc',5))             # exception

    print(read_file('seneca2.txt')) # works (file made in lab5b)

    print(read_file('file10000.txt')) # exception
