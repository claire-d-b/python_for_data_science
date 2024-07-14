def filter(function: any, L: list, n: int):
    ret = []
    """ applies given function to each item of the list """
    for item in L:
        if function(item, n):
            ret.append(item)
    return ret
