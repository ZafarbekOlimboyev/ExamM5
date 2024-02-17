import math

def tub(x: int):
    for i in range(3,int(math.sqrt(x)+1),2):
        if x % i == 0:
            return 0
        else:
            continue
    return x
def sonlar(n: int):
    if n > 2:
        yield 2
        for i in range(3,n,2):
            if tub(i) != 0:
                yield i
    elif n == 2:
        yield 2
    else:
        yield "Tub son yo'q"

if __name__ == '__main__':
    n = int(input("N ni kiriting : "))
    print(list(sonlar(n)))


# intput : 100          output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# input : 2             output: [2]
# input : 0             output: ["Tub son yo'q"]