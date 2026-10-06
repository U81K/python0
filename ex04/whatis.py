import sys

if (len(sys.argv) > 2):
    print("AssertionError: more than one argument is provided")

if len(sys.argv) == 2:
    try:
        n = int(sys.argv[1])
        if (n % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument must be an integer")
