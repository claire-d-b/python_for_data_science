from sys import argv

def main():
# your tests and your error handling

    key = 0
    args = []
    kwargs = {}
    if len(argv[1:]) == 0:
        while True:
            try:
                args = input()
            except EOFError:
                break
    for arg in argv[1:]:
        value = arg
        kwargs[key] = value
        args.append(arg)
        key += 1

    punctuation = {'.', ',', ';', ':', '!', '?', '\'', '"', '(', ')', '[', ']', '{', '}', '-', '_', '/', '\\', '|', '@', '#', '$', '%', '^', '&', '*', '<', '>', '~', '`'}
    if len(argv[1:]) > 0:
        print("The text contains " + str(len(*args)) + " characters: ")
    else:
        print("The text contains " + str(len(args)) + " characters: ")
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