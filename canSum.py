def sum(target_sum, numbers, memo = {}):

    
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for i in numbers:
        remainder = target_sum - i

        if sum(remainder, numbers, memo):
            memo[remainder] = True
    
    return False



print(sum(7, [2,3]))