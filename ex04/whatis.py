from sys import argv

def main():
    args = []
    kwargs = {}
    key = 0
    """ catches program argument """
    for arg in argv[1:]:
        value = arg
        kwargs[key] = value
        args.append(arg)
        key += 1
    
    try:
        assert len(args) <= 2, "more than one argument is provided"
    except AssertionError as e:
            print(f"AssertionError: {e}")
    if len(args) <= 2:
        """ check whether arg is valid and is an even/odd number """
        try:
            for args, kwargs in enumerate(kwargs):
                assert arg.isdigit(), "argument is not an integer"
                if int(arg) % 2:
                    print("I'm odd")
                else:
                    print("I'm even")
        except AssertionError as e:
            print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()

