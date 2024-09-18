def isValid(s):
    p = []
    m = {')': '(', ']': '[', '}': '{'}

    for v in s:
        if v in m.values():
            p.append(v)
        elif v in m.keys() :
            if p and m[v] == p[-1]:
                p.pop()
            else:
                return False
        else:
            return False
    
    if len(p) == 0:
        return True
    else:
        return False