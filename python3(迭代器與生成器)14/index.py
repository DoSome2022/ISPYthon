#--- next()

list=[1,2,3,4]
it = iter(list)

# print(next(it))
# print(next(it))

list=[1,2,3,4]
it = iter(list)    # 創建迭代器對象
for x in it:
    print (x, end=" ")

#----

import sys

def fibonacci(n): # 生成器函數 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一個迭代器，由生成器返回生成

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()