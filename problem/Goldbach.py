def Goldbach(a):
    import math
    a = int(a)
    x = int(a/2+1)
    if a % 2 == 0 and a > 4:
        for i in range(3,x,2):
            for j in range(2, int(math.sqrt(i) + 1)):
                if i % j == 0:
                    break
            else:
                for j in range(2, int(math.sqrt(a-i) + 1)):
                    if (a-i) % j == 0:
                        break
                else:
                    print(i,a-i)
    elif a == 4:
        print(2,2)
    else:
        print("ERROR")
