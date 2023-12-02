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
                i+=1
        print("{}".format(counter))

# Write a program that prints the result of the addition of all arguments

# The output should be the result of the addition of all arguments, followed by a new line
# You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
# Your code should not be executed when imported

