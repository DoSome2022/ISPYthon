a = (1991, 2014, 'physics', 'math')
print(a, type(a), len(a))


tup = (1, 2, 3, 4, 5, 6)
print(tup[0], tup[1:5])

tup1 = () # 空元组
tup2 = (20,) # 一個元素，需要在元素後添加逗號  

tup1, tup2 = (1, 2, 3), (4, 5, 6)
print(tup1+tup2)