[來源](https://www.w3cschool.cn/python3/) 

## Python3 迭代器與生成器

---

##  迭代器

迭代是Python 最強大的功能之一，是訪問集合元素的一種方式。。

迭代器是一個可以記住遍歷的位置的對象。

迭代器對像從集合的第一個元素開始訪問，直到所有的元素被訪問完結束。迭代器只能往前不會後退。

迭代器有兩個基本的方法：iter()和next()。

字符串，列表或元組對像都可用於創建迭代器：

```
list=[1,2,3,4]
it = iter(list)

print(next(it))
print(next(it))
```
迭代器對象可以使用常規for 語句進行遍歷：  
```
list=[1,2,3,4]
it = iter(list)    # 創建迭代器對象
for x in it:
    print (x, end=" ")
```
(index.py)

---
## 生成器  

在Python 中，使用了yield 的函數被稱為生成器（generator）。

跟普通函數不同的是，生成器是一個返回迭代器的函數，只能用於迭代操作，更簡單點理解生成器就是一個迭代器。

在調用生成器運行的過程中，每次遇到yield 時函數會暫停並保存當前所有的運行信息，返回yield 的值。並在下一次執行next() 方法時從當前位置繼續運行。

以下實例使用yield 實現斐波那契數列：
```
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
```
(index.py)

---