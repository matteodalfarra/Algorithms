def next_smaller(n):
    if n < 10:
        return -1

    s = list(str(n))
    for i in range(len(s)-1, 0, -1):
        if int(s[i]) < int(s[i-1]):
            max = i
            for j in range(i, len(s)):
                if int(s[j]) < int(s[i-1]) and int(s[j]) > int(s[max]):
                    max = j
            s[i-1], s[max] = s[max], s[i-1]
            s = s[:i] + sorted(s[i:], reverse=True)

            if int(s[0]) == 0:
                return -1
            return int("".join(s)) 
    return -1