from is_perfect import is_perfect
def my_filter(x):
    a = range(1,x + 1)
    def mf(function):
        for i in a:
            if is_perfect(i) == 1:
                print(i)
    return mf
