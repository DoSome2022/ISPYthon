[來源](https://www.w3cschool.cn/python3/)  

模塊是一個包含所有你定義的函數和變量的文件，其後綴名是.py。模塊可以被別的程序引入，以使用該模塊中的函數等功能。這也是使用Python 標準庫的方法。下面是一個使用Python 標準庫中模塊的例子。 

```
import sys

print('命令行參數如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路徑為：', sys.path, '\n')

```

(index.py)

1、import sys 引入Python 標準庫中的sys.py 模塊；這是引入某一模塊的方法。  
2、sys.argv 是一個包含命令行參數的列表。  
3、sys.path 包含了一個Python 解釋器自動查找所需模塊的路徑的列表。  

---

## import 語句

如果要使用Python 源文件，只需在另一個源文件裡執行import 語句，import 語句語法如下：
```
import module1[,module2[, ... moduleN]
```

當解釋器遇到import 語句，如果模塊在當前的搜索路徑就會被導入。

搜索路徑是一個解釋器會先進行搜索的所有目錄的列表。如果想要導入模塊support，需要把命令放在腳本的頂端：

```
# filename:support.py
def print_func( par ):
    print ("Hello : ", par)
    return

```
(support.py)
index.py 引入 support模塊：
```
import support

support.print_func('okok')

```
(index.py)
一個模塊只會被導入一次，不管你執行了多少次import。這樣可以防止導入模塊被一遍又一遍地執行。

當我們使用import 語句的時候，Python 解釋器是怎樣找到對應的文件的呢？

這就涉及到Python 的搜索路徑，搜索路徑是由一系列目錄名組成的，Python 解釋器就依次從這些目錄中去尋找所引入的模塊。

---

因此若像我一樣在當前目錄下存在與要引入模塊同名的文件，就會把要引入的模塊屏蔽掉。

了解了搜索路徑的概念，就可以在腳本中修改sys.path 來引入一些不在搜索路徑中的模塊。

代碼如下：
fibo.py
```
def fib(n):    # 定義到 n 的斐波那契數列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
def fib2(n): # 返回到 n 的斐波那契數列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

```
導入這個 fibo 模塊：

index.py
```

import fibo

fibo.fib(10)

print(fibo.fib2(20))

print(fibo.__name__)
```

---

##  from ... import 語句

Python 的from 語句讓你從模塊中導入一個指定的部分到當前命名空間中，語法如下:

```
from modname import name1[, name2[, ... nameN]
```

例如，要導入模塊fibo 的fib 函數，使用如下語句:
```
from fibo import fib, fib2
```
這個聲明不會把整個fibo 模塊導入到當前的命名空間中，它只會將fibo 裡的fib 函數引入進來。

---

## from ... import * 語句  
把一個模塊的所有內容全都導入到當前的命名空間也是可行的，只需使用如下聲明：
```
from modname import *
```
這提供了一個簡單的方法來導入一個模塊中的所有項目。然而這種聲明不該被過多的使用。

---

##  __name__屬性

一個模塊被另一個程序第一次引入時，其主程序將運行。如果我們想在模塊被引入時，模塊中的某一程序塊不執行，我們可以用__name__ 屬性來使該程序塊僅在該模塊自身運行時執行。

```
if __name__ == '__main__':
    print('程序自身在運行')
else:
    print('我來自另一模塊')
```
(index.py)

- 每個模塊都有一個__name__ 屬性，當其值是'__main__' 時，表明該模塊自身在運行，否則是被引入。
- 每個__name__ 與__main__ 底下是雙下劃線，是“_ _”去掉中間的空格。

---
## dir()

```
#內置的函數 dir() 可以找到模塊內定義的所有名稱。以一個字符串列表的形式返回:
import fibo , sys

print(dir(fibo))
print(dir(sys))
```

(index.py)

---