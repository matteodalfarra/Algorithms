def to_weird_case(words):
    words = words.split(" ")
    s = ""
    
    for word in words:
        for i in range(len(word)):
            if i % 2 == 0:
                s += word[i].upper()
            else:
                s += word[i].lower()

        s += " "
    else:
        s = s[0:len(s)-1]
    
    return s