def solution(s):
    if len(s) > 0:
        couple = []

        for i in range(0,len(s),2):
            couple.append(s[i:i+2])

        if len(couple[-1]) == 1:
            couple[-1] += "_" 
        return couple
    else:
        return []