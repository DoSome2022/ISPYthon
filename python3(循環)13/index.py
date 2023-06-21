#--- while loop

# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter     
#     counter += 1  
# print('Sum of 1 until %d: %d' % (n,sum)) 

#--- for loop

# DC = ['BvS','水水俠','神奇女俠','大超回歸']
# for x in DC:
#  print (x)

#--- range()

# for i in range(10):
#  print(i)

# 你也可以使用range 指定區間的值：
# for i in range(5,9) :
#   print(i)

#也可以使range 以指定數字開始並指定不同的增量

# for i in range(0, 10, 3) :
#     print(i)

#負數：
# for i in range(-10, -100, -30) :
#    print(i)

#--- range() + len()

# aa = ['a','s','d','f','g']
# for i in range(len(aa)):
#     print(i, aa[i])


# pp =list(range(5))
# print(pp)

for n in range(2, 10):
     for x in range(2, n):
        if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # 循環中沒有找到元素
        print(n, 'is a prime number')

