def my_sum(a=0,*args):
    b = 0
    for i in args:
        b = b + i
    return a + b
