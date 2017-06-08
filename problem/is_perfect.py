def is_perfect(n):
    import math
    a = 0
    for i in range(1,int(math.sqrt(n)+1)):
        if n % i == 0:
            if i == n/i:
                a = a + i
            else:
                a = a + i + n/i
    if a == 2*n:
        return True
    else:
        return False
