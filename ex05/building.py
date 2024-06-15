from sys import argv

def set_args(args, kwargs):
    key = 0
    for arg in argv[1:]:
        value = arg
        kwargs[key] = value
        args.append(arg)
        key += 1

def main():
# your tests and your error handling
    args = []
    kwargs = {}

    set_args(args, kwargs)
    try:
        assert len(args) <= 2, "more than one argument is provided"
    except AssertionError as e:
            print(f"AssertionError: {e}")

    finally:
        punctuation = {'.', ',', ';', ':', '!', '?', '\'', '"', '(', ')', '[', ']', '{', '}', '-', '_', '/', '\\', '|', '@', '#', '$', '%', '^', '&', '*', '<', '>', '~', '`'}
        print("The text contains " + str(len(*args)) + " characters: ")
        i = 0
        for arg in args:
            for item in arg:
                if item.isupper():
                    i += 1
        print(str(i) + " upper letters")
        i = 0
        for arg in args:
            for item in arg:
                if item.islower():
                    i += 1
        print(str(i) + " lower letters")
        i = 0
        for arg in args:
            for item in arg:
                if item in punctuation:
                    i += 1
        print(str(i) + " punctuation marks")
        i = 0
        for arg in args:
            for item in arg:
                if item.isspace():
                    i += 1
        print(str(i) + " spaces")
        i = 0
        for arg in args:
            for item in arg:
                if item.isdigit():
                    i += 1
        print(str(i) + " digits")

if __name__ == "__main__":
    main()