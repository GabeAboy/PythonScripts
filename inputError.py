def int_input(*args, **kwargs):
    try:
        return int(raw_input(*args, **kwargs))
    except ValueError:
        print("Please, sucker, enter a valid integer")
        return int_input(*args, **kwargs)

num = int_input("Enter a number: ")
