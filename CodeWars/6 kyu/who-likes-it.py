def likes(names):
    length = len(names)
    if length == 0:
        return 'no one likes this'
    elif length == 1:
        return names[0] + ' likes this'
    
    str = ''
    for idx, i in enumerate(names):
        
        if length > 3:
            str += names[idx] + ', ' + names[idx + 1] 
            str += f' and {length - 2} others'
            break
        else:
            str += i
            if idx < length - 2:
                str += ', '
            elif idx < length - 1:
                str += ' and '
            
            
    str += ' like this'

        
    return str

    # https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python