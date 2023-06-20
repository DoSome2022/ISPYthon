a = ['him', 25, 100, 'her']
print(a)

b = [1, 2, 3, 4, 5]
bb=b + [6, 7, 8]
print(b)
print(bb)


c = [1, 2, 3, 4, 5, 6]
c[0] = 9
c[2:5] = [13, 14, 15]
print(c)

c[2:5] = []   # 删除
print(c)