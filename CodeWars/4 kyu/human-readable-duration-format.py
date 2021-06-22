def format_duration(seconds):
    import math
    minutes = 60
    hours = 60*60
    days = 60*60*24
    years = 60*60*24*365
    s = m = h = d = y = 0
    

    if seconds == 0:
        return 'now'
        
    if seconds >= years:
        y = math.floor(seconds / years)
        seconds -= y * years
        d = math.floor(seconds / days)
        seconds -= d * days
        h = math.floor(seconds / hours)
        seconds -= h * hours
        m = math.floor(seconds / minutes)
        seconds -= m * minutes
        s = seconds    
    elif seconds >= days:
        d = math.floor(seconds / days)
        seconds -= d * days
        h = math.floor(seconds / hours)
        seconds -= h * hours
        m = math.floor(seconds / minutes)
        seconds -= m * minutes
        s = seconds
    elif seconds >= hours:
        h = math.floor(seconds / hours)
        seconds -= h * hours
        m = math.floor(seconds / minutes)
        seconds -= m * minutes
        s = seconds
    elif seconds >= minutes:
        m = math.floor(seconds / minutes)
        seconds -= m * minutes
        s = seconds
    else:
        s = seconds


    dic = {}
    l = [y, d, h, m, s]
    d = ['year', 'day', 'hour', 'minute', 'second']
    for i, j in zip(l, d):
        if i == 0:
            continue
        dic[j] = i
    
    str = ''
    
    length = len(dic)
    for i, j in dic.items():
        str += f'{j} {i}'
        if j > 1:
            str += 's'
        if length > 2:
            str += ', '
        elif length > 1:
            str += ' and '
            
        length -= 1
        
    return str.strip()


    # https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python