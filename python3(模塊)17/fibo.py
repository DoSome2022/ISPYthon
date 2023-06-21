def fib(n):    # 定義到 n 的斐波那契數列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
def fib2(n): # 返回到 n 的斐波那契數列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result