from ft_filter import filter

def count_chars(chars: any):
    try:
        str(chars)
        return True
    except ValueError:
        return False

def count_digits(chars: any):
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