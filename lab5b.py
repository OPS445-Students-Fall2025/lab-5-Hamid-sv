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
def append_file_string(file_name, string_of_lines):

    """Append the whole string to the end of file_name."""

    with open(file_name, 'a') as f:

        f.write(string_of_lines)



def write_file_list(file_name, list_of_lines):

    """Overwrite file_name with every list item on its own line."""

    with open(file_name, 'w') as f:

        for line in list_of_lines:

            f.write(line + '\n')



def copy_file_add_line_numbers(file_name_read, file_name_write):

    """Copy lines from file_name_read to file_name_write, prefixing 'N:'."""

    # read (stripping newlines)

    with open(file_name_read, 'r') as r:

        lines = r.read().splitlines()

    # write numbered

    with open(file_name_write, 'w') as w:

        for i, line in enumerate(lines, start=1):

            w.write(f"{i}:{line}\n")
if __name__ == '__main__':

    file1 = 'seneca1.txt'

    file2 = 'seneca2.txt'

    file3 = 'seneca3.txt'

    string1 = 'First Line\nSecond Line\nThird Line\n'

    list1 = ['Line 1', 'Line 2', 'Line 3']



    append_file_string(file1, string1)

    print(read_file_string(file1))



    write_file_list(file2, list1)

    print(read_file_string(file2))



    copy_file_add_line_numbers(file2, file3)

    print(read_file_string(file3))
