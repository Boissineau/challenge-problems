def next_bigger(n):
    

    l = [x for x in str(n)]
    tmp = l
    length = len(l)
    num = ''
    idx = length - 1
    print(n)
    changed = False
    while(idx != 0):
        if l[idx - 1] is not None:
            if l[idx] > l[idx-1]:
                print(f'switching {l[idx-1]} with {l[idx]}')
                t = l[idx-1]
                tmp[idx-1] = l[idx]
                tmp[idx] = t
                for i in tmp:
                    num += i
                if int(num) > n:
                    print(num)
                    changed = True
                    break
        idx -= 1
    if changed == False:
        return -1
        
    sub = [x for x in num]
    sub2 = sub[idx:]
    sub2.sort()


    for i in range(len(sub2)):
        sub[idx + i] = sub2[i]
    
    ret = ''
    for i in sub:
        ret += i 

    
    return int(ret)
    
    
    
    
    
    
    
    
    # https://www.codewars.com/kata/55983863da40caa2c900004e/train/python