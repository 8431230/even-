import sys

for arg in sys.argv[1:]:
    try:
        number = int(arg)
        if (number % 2) == 0:
            print(f"{number}: Even number")
        else:
            print(f"{number}: Odd number")
    except ValueError:
        print(f"Error: '{arg}' is not a valid integer")
