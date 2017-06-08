def fib(n=0):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>=2:
        return fib(n-1) + fib(n-2)
# n = 100　で時間がかかりすぎた一度計算した結果を保存しておくと速くできるらしい
