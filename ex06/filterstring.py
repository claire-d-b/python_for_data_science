from sys import argv
from ft_filter import filter

def count_chars(chars: any):
    """     counts occurences of chars """
    try:
        str(chars)
        return True
    except ValueError:
        return False

def count_digits(chars: any):
    """     count occurences of digits """
    try:
        int(chars)
        return True
    except ValueError:
        return False

def main():
    key = 0
    args = []
    kwargs = {}
    """ catches program argument """
    for arg in argv[1:]:
        value = arg
        kwargs[key] = value
        args.append(arg)
        key += 1

    try:
        assert len(args), "the arguments are bad"
        assert count_chars(args[0]), "the arguments are bad"
        assert count_digits(args[1]), "the arguments are bad"
    except AssertionError as e:
            print(f"AssertionError: {e}")
            return
    words = args[0].split()
    n = int(args[1])
    print(filter(lambda words, n: len(words) >= n, words, n))
    

if __name__ == "__main__":
    main()