def number_of_routes(m, n, memo = {}):
    key = str(m) + ',' + str(n)

    if key in memo:
        return memo[key]
    
    if m == 0 or n == 0:
        return 1
    memo[key] = number_of_routes(m-1, n) + number_of_routes(m, n-1) 
    return memo[key]   


import math
def routes(n):
    if n <= 0:
        return 0
    return (math.factorial(2*n)//math.factorial(n)//math.factorial(n))


# https://www.codewars.com/kata/56a127b14d9687bba200004d/train/python
# https://www.codewars.com/kata/559aa1295f5c38fd7b0000ac/solutions/python