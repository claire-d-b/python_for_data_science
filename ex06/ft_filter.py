def filter(function: any, L: list, n: int):
    ret = []
    """     applies given function to each item of the list """
    for l in L:
        if function(l, n) == True:
            ret.append(l)
    return ret
    