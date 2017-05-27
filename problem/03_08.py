import math
a = 0
n = input("完全数であるか調べたい自然数を入力してください ")
n = int(n)
if n % 1 == 0:
    if n > 0:
        for i in range(1,int(math.sqrt(n)+1)):
            if n % i == 0:
                if i == n/i:
                    a = a + i
                else:
                    a = a + i + n/i
        if a == 2*n:
            print("TRUE")
        else:
            print("FALSE")
    else:
        print("正数を入力してください")
else:
    print("整数を入力してください")
