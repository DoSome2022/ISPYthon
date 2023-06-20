a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
    print ("1 - 變量 a 在給定的列表中 list 中")
else:
    print ("1 - 變量 a 不在給定的列表中 list 中")

if ( b not in list ):
    print ("2 - 變量 b 不在給定的列表中 list 中")
else:
    print ("2 - 變量 b 在給定的列表中 list 中")

# 修改變量 a 的值
a = 2
if ( a in list ):
    print ("3 - 變量 a 在給定的列表中 list 中")
else:
    print ("3 - 變量 a 不在給定的列表中 list 中")