#!/usr/bin/python3

if __name__ == "__main__":
    """Print the result of addition of all arguments."""
    import sys

    counter = 0
    i = 1
    if len(sys.argv) > 0:
        while i < len(sys.argv):
            if sys.argv[i] != '':
                counter += int(sys.argv[i])
                i += 1
        print("{}".format(counter))
