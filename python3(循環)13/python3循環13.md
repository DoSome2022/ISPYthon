[來源](https://www.w3cschool.cn/python3/)  

## Python3 循環

介紹Python 循環語句的使用。

Python 中的循環語句有for 和while。

Python 循環語句的控制結構圖如下所示：

<img src="https://atts.w3cschool.cn/attachments/uploads/2014/05/while_loop_1.png">

---
## while 循環
Python 中while 語句的一般形式：
```
while 判斷條件：
    statements
```
同樣需要注意冒號和縮進。另外，在Python中沒有do-while 循環。

以下實例使用了while 來計算1 到100 的總和：
```
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter     
    counter += 1  
print('Sum of 1 until %d: %d' % (n,sum)) 
```
執行結果如下：
```
Sum of 1 until 100: 5050
```
(index.py)

---

## for 語句

Python for 循環可以遍歷任何序列的項目，如一個列表或者一個字符串。

for 循環的一般格式如下：

```
for <variable> in <sequence>:
  <statements>
else:
 <statements>
```

Python for循環實例：
```
DC = ['BvS','水水俠','神奇女俠','大超回歸']

for x in DC:
 print (x)
```
執行結果如下：
```
BvS
水水俠
神奇女俠
大超回歸
```
(index.py)

---

## range()函數  

如果你需要遍歷數字序列，可以使用內置range() 函數。它會生成數列，例如:

```
for i in range(10):
 print(i)

# 你也可以使用range 指定區間的值：
for i in range(5,9) :
  print(i)

#也可以使range 以指定數字開始並指定不同的增量
for i in range(0, 10, 3) :
    print(i)

#負數：
for i in range(-10, -100, -30) :
   print(i)  
   
```
(index.py)

您可以結合range() 和len() 函數以遍歷一個序列的索引,如下所示:

```
#--- range() + len()

aa = ['a','s','d','f','g']
for i in range(len(aa)):
    print(i, aa[i])

```
(index.py)

可以使用range() 函數來創建一個列表：
```
pp =list(range(5))
print(pp)
```
(index.py)
---

## break 和continue 語句及循環中的else 子句   

break 語句可以跳出for 和while 的循環體。如果你從for 或while 循環中終止，任何對應的循環else 塊將不執行。

continue 語句被用來告訴Python 跳過當前循環中的當此循環，然後繼續進行下一輪循環。

循環語句可以有else 子句；它在窮盡列表(以for 循環)或條件變為假(以while 循環)循環終止時被執行，但循環被break 終止時不執行，如下查尋質數的循環例子:

```
for n in range(2, 10):
     for x in range(2, n):
        if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # 循環中沒有找到元素
        print(n, 'is a prime number')

```

---

## pass 語句

pass 語句什麼都不做。它只在語法上需要一條語句但程序不需要任何操作時使用。例如:

```
while True:
     pass
```
最小的類:
```
 class MyEmptyClass:
    pass

```

---