def solution(args):
    if len(args) == 1:
        return str(args[0])          
    elif len(args) > 1:
        start = args[0]
        end = args[0]
    else:
        return ''
    
    list_segments = []

    for i in range(1, len(args)):
        end = args[i-1]
        if args[i] != args[i-1] + 1:
            if start != end:
                if start == end - 1:
                    list_segments.append(f'{start},{end}')
                else:
                    list_segments.append(f'{start}-{end}')
            else:
                list_segments.append(f'{start}')
            start = args[i]
    else: 
        end = args[len(args) - 1]
        if start != end:
            if start == end - 1:
                list_segments.append(f'{start},{end}')
            else:
                list_segments.append(f'{start}-{end}')
        else:
            list_segments.append(f'{start}')

    return ','.join(list_segments)
