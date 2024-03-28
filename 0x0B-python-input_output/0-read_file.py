#!/usr/bin/python3
"""Read a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Read a text file

    Args:
        filename(str): file name and return it to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
