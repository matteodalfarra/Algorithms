def next_bigger(n):
    if n < 10:
        return -1
    
    s = list(str(n))
    for i in range(len(s)-1, 0, -1):
        if int(s[i]) > int(s[i-1]):
            min = i
            for j in range(i, len(s)):
                if s[j] > s[i-1] and s[j] < s[min]:
                    min = j
            s[i-1], s[min] = s[min], s[i-1]
            s = s[:i] + sorted(s[i:])
            return int("".join(s)) 
    return -1