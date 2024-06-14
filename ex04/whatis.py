from sys import argv

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
    
    try:
        assert len(args) <= 2, "more than one argument is provided"
    except:
        print("AssertionError: more than one argument is provided")
    if len(args) <= 2:
        try:
            for args, kwargs in enumerate(kwargs):
                assert arg.isdigit(), "argument is not an integer"
                if int(arg) % 2:
                    print("I'm odd")
                else:
                    print("I'm even")
        except:
            print("AssertionError: argument is not an integer")

if __name__ == "__main__":
    main()

