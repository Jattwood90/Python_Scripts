"""From codewars"""

def tribonacci(signature, n):
    if n ==0:
        return []

    a, b, c = signature[0], signature[1], signature[2]
    output = [a,b,c]

    if n == 1:
        return [a]


    for i in range(n-3):
        total = a+b+c
        a = b
        b = c
        c = total
        output.append(c)
    return output