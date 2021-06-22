def find_it(seq):
    
    for i in seq:
        count = 0
        for j in seq:
            if j == i:
                count += 1
        if count % 2 != 0:
            return i


# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python