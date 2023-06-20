a = 10
b = 20

if ( a and b ):
    print ("1 - 變量 a 和 b 都為 true")
else:
    print ("1 - 變量 a 和 b 有一個不為 true")

if ( a or b ):
    print ("2 - 變量 a 和 b 都為 true，或其中一個變量為 true")
else:
    print ("2 - 變量 a 和 b 都不為 true")

# 修改變量 a 的值
a = 0
if ( a and b ):
    print ("3 - 變量 a 和 b 都為 true")
else:
    print ("3 - 變量 a 和 b 有一個不為 true")

if ( a or b ):
    print ("4 - 變量 a 和 b 都為 true，或其中一個變量為 true")
else:
    print ("4 - 變量 a 和 b 都不為 true")

if not( a and b ):
    print ("5 - 變量 a 和 b 都為 false，或其中一個變量為 false")
else:
    print ("5 - 變量 a 和 b 都為 true")