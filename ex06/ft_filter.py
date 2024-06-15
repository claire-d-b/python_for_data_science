def filter(function: any, L: list):
    ret = []
    for l in L:
        if function(l) == True:
            ret.append(l)
    return ret