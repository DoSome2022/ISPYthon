a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
# a.insert(2, -1)
# a.append(333)

# print(a)
# print( a.index(333) )

# a.remove(333)
# print(a)

# a.reverse()
# print(a)

# a.sort()
# print(a)

#----  將列表當做堆棧使用
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)

# print(stack)

# stack.pop()
# print(stack.pop())
# print(stack)

# stack.pop()
# print(stack.pop())
# print(stack)


# stack.pop()
# print(stack.pop())
# print(stack)


# print(stack)

vec = [2, 4, 6]
vec2 = [3*x for x in vec]
print(vec2)


freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruit2 = [weapon.strip() for weapon in freshfruit]

print(freshfruit2)



matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

#兩個方法

list1 = [[row[i] for row in matrix] for i in range(4)]
print(list1)


transposed = []
for i in range(4):
     transposed.append([row[i] for row in matrix])

print(transposed)


#--- 元組和序列 

t = 12345, 54321, 'hello!'

print(t[0])
print(t)

u = t, (1, 2, 3, 4, 5)

print(u)

#--- 集合

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)
print('orange' in basket )
print( 'crabgrass' in basket )

a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b  )
print(a | b )
print(a & b)
print(a ^ b  )

aa = {x for x in 'abracadabra' if x not in 'abc'}

print(aa)

#--- 字典
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel.keys()))

print(sorted(tel.keys()))

print('guido' in tel)
print('jack' not in tel)

#構造函數dict() 直接從鍵值對元組列表中構建字典。如果有固定的模式，列表推導式指定特定的鍵值對：

ccc = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

print(ccc)
# 字典推導可以用來創建任意鍵和值的表達式詞典：
bbb = {x: x**2 for x in (2, 4, 6)}
print(bbb)
#如果關鍵字只是簡單的字符串，使用關鍵字參數指定鍵值對有時候更方便：

aaa = dict(sape=4139, guido=4127, jack=4098)


