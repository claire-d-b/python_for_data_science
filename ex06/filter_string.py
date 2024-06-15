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
    print(filter(count_chars, "lalala"))
    print(filter(count_digits, "lalala"))

if __name__ == "__main__":
    main()