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
        assert len(args) < 2, "more than one argument is provided"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return
    if len(args) <= 2:
        """ check whether arg is valid and is an even/odd number """
        try:
            for args, kwargs in enumerate(kwargs):
                assert str(arg).isdigit(), "argument is not an integer"
                if abs(int(arg)) % 2:
                    print("I'm Odd")
                else:
                    print("I'm Even")
        except AssertionError as e:
            print(f"AssertionError: {e}")

