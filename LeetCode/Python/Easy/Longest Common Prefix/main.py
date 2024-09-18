def longestCommonPrefix(strs):
    if len(strs) < 2:
        return strs[0]
    mLen = min(map(len, strs))
    prefix = ""
    for i in range(0, mLen, 1):
        char = strs[0][i]
        for s in strs[1:]:
            if s[i] != char:
                return prefix
        else:
            prefix += char
    return prefix