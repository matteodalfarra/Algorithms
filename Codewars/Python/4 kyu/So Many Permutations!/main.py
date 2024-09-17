import itertools as it

def permutations(s):
    if (len(s) > 0):
        perm = set(''.join(p) for p in it.permutations(s))
        return perm
    else:
        return s