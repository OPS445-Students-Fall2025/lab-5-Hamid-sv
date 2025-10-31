#!/usr/bin/env python3

# Author ID: Ssamadi   # (use your Seneca ID string as your instructor expects)



def read_file_string(file_name):

    """Return entire file contents as ONE string."""

    # 'with' auto-closes the file even if an error occurs

    with open(file_name, 'r') as f:

        return f.read()



def read_file_list(file_name):

    """Return entire file as a list of lines WITHOUT newline chars."""

    # .splitlines() removes the trailing '\n' safely

    with open(file_name, 'r') as f:

        return f.read().splitlines()



if __name__ == '__main__':

    file_name = 'data.txt'

    print(read_file_string(file_name))

    print(read_file_list(file_name))
