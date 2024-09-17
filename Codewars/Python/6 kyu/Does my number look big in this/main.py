def narcissistic( value ):
    l = len(str(value))
    total = 0
    for i in str(value):
        total += int(i) ** l
    
    if total == value:
        return True
    else:
        return False