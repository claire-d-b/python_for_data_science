def filter(function: any, L: list, n: int):
    """ applies given function to each item of the list """
    ret = list([item for item in L if function(item, n)])
    return ret
