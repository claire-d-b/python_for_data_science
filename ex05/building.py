from sys import argv


def main():
    key = 0
    args = []

    punctuation = {'.', ',', ';', ':', '!', '?', '\'', '"', '(', ')',
                   '[', ']', '{', '}', '-', '_', '/', '\\', '|', '@',
                   '#', '$', '%', '^', '&', '*', '<', '>', '~', '`'}

    spaces = {'\t', '\n', '\r', '\v', '\f', ' '}

    """ if there is no command-line arg, prompt for user input """
    if len(argv[1:]) == 0:
        arg = ''
        while True:
            try:
                arg = input()
            except EOFError:
                break
            except KeyboardInterrupt:
                break
        print("The text contains " + str(len(arg)) + " characters: ")
        args.append(arg)

    else:
        """ catches program argument """
        for arg in argv[1:]:
            args.append(arg)
            key += 1

    """ count occurences of below char ranges """
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
            if item in spaces:
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

# In Python, __name__ is a special variable assigned to the name of the Python module
# by the interpreter. If your module is invoked as a script, then the string ‘__main__’
# will automatically be assigned to the special variable __name__.
# But if you import your module into another module, the string ‘my_module’ will be assigned to __name__.
# When a module is invoked as a string, then Python interpreter will assign the string '__main__'
# to a special variable called __name__, and the code, which is defined under the condition
# if __name__ == ‘__main__', will subsequently get executed. 
# On the other hand, when a module is imported in another module, then the Python interpreter
# will assign the string with the name of that module to the special variable __name__.
# This means that in such cases if __name__ == ‘__main__’ will evaluate to False which means that
# only the code outside of this condition will get executed once imported.
