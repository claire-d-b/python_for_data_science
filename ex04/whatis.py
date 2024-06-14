from sys import argv, getsizeof

def main():
    args = []
    kwargs = {}
    key = 0
    for arg in argv[1:]:
        value = arg
        kwargs[key] = value
        args.append(arg)
        key += 1
    # print(args)
    # print(kwargs)
    assert getsizeof(args) > 1, "more than one argument is provided"
    try:
        for args, kwargs in enumerate(kwargs):
            try:
                if int(arg) % 2:
                    print("I'm odd")
                else:
                    print("I'm even")
            except:
                print("argument is not an integer")
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()


