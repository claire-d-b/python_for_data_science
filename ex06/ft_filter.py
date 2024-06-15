def filter(function: any, L: list):
    ret = []
    """     applies given function to each item of the list """
    for l in L:
        if function(l) == True:
            ret.append(l)
    return ret