a = 20
b = 20

if ( a is b ):
    print ("1 - a 和 b 有相同的標識")
else:
    print ("1 - a 和 b 沒有相同的標識")

if ( id(a) == id(b) ):
    print ("2 - a 和 b 有相同的標識")
else:
    print ("2 - a 和 b 沒有相同的標識")

# 修改變量 b 的值
b = 30
if ( a is b ):
    print ("3 - a 和 b 有相同的標識")
else:
    print ("3 - a 和 b 沒有相同的標識")

if ( a is not b ):
    print ("4 - a 和 b 沒有相同的標識")
else:
    print ("4 - a 和 b 有相同的標識")