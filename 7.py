def next_bigger(n):
    
    l = [x for x in str(n)]

    length = len(l) - 1
    for i in range(length):
        if l[length - i] is not None and l[length - 1 - i] is not None:
            if l[length - i] > l[length - 1 - i]:
                tmp = l[length - 1 - i]
                l[length - 1 - i] = l[length - i]
                l[length - i] = tmp
                break
    
    
    
    
    num = ''
    for i in l:
        num += i
    print(num)

    return int(num)
    
    
    # https://www.codewars.com/kata/55983863da40caa2c900004e/train/python