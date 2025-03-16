import sys

assert len(sys.argv) <= 2, "AssertionError: more than one argument is provided"

if len(sys.argv) == 2:
    try:
        num = int(sys.argv[1])
    except ValueError:
        raise AssertionError("AssertionError: argument is not an integer")

    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
