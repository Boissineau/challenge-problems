def dirReduc(arr):
    
    dic = {
        'NORTH': 1,
        'SOUTH': 2,
        'EAST': 10,
        'WEST': 11
    }

    
    current = []
    for direction in arr:
        print(current)
        value = dic.get(direction)
        if len(current) > 0:
            last = dic.get(current[-1])
            if len(current) > 0 and (value == last - 1 or value == last + 1):
                current.pop()
                continue
        current.append(direction)
    return current


# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
