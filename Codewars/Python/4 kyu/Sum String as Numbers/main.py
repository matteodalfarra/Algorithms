def sum_strings(x, y):    
    x = x.lstrip('0') or '0'
    y = y.lstrip('0') or '0'

    if len(x) > len(y):
        y = y.zfill(len(x))
    elif len(y) > len(x):
        x = x.zfill(len(y))
    
    sum = []
    carry = 0
    for i in range(len(x)-1, -1, -1):
        if carry > 0:
            actSum = str(int(x[i]) + int(y[i]) + carry)
            carry = 0
        else:
            actSum = str(int(x[i]) + int(y[i]))

        if int(actSum) > 9:
            actSum = actSum[len(actSum)-1]
            carry = 1

        sum.append(actSum)
    if carry > 0:
        return str(carry) + "".join(sum[::-1])
    else:
        return "".join(sum[::-1])