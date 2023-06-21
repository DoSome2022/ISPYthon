[來源](https://www.w3cschool.cn/python3/)  

##  Python3 函數  
本章節我們將為大家介紹Python 中函數的應用。

Python 定義函數使用def 關鍵字，一般格式如下：

```
def  函数名（参数列表）：
    函数体

```
讓我們使用函數來輸出"Hello World！"：
```
def hello():
    print("hello World!")

hello()
```
更複雜點的應用，函數中帶上參數變量:
```
def area(width, height):
    return width * height
 
def print_welcome(name):
    print("Welcome", name)

print_welcome("Fred")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))
```
輸出結果：  
```
Welcome Fred
width = 4  height = 5  area = 20
```  
---  
## 函數變量作用域  
定義在函數內部的變量擁有一個局部作用域，定義在函數外的擁有全局作用域。

通過以下實例，你可以清楚了解Python 函數變量的作用域：  
```
a = 4  # 全局變量
 
def print_func1():
    a = 17 # 局部變量
    print("in print_func a = ", a)


def print_func2():   
    print("in print_func a = ", a)


print_func1()
print_func2()
print("a = ", a)

```
運行結果 :
```
in print_func a =  17
in print_func a =  4
a =  4

```

(index.py)

##  關鍵字參數  
函數也可以使用kwarg = value 的關鍵字參數形式被調用。例如，以下函數:
```
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```  
可以以下幾種方式被調用:  
```
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

```
以下為錯誤調用方法：
```
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument

```
---

## 返回值  
Python 函數使用return 語句返回函數值，可以將函數作為一個值賦值給指定變量：  
```
def return_sum(x,y):
    c = x + y
    return c


res = return_sum(4,5)
print(res)
```
---

## 可變參數列表

最後，一個較不常用的功能是可以讓函數調用可變個數的參數。

這些參數被包裝進一個元組(查看元組和序列)。

在這些可變個數的參數之前，可以有零到多個普通的參數:

```
def arithmetic_mean(*args):
    if len(args) == 0:
        return 0
    else:
        sum = 0
        for x in args:
            sum += x
        return sum/len(args)


print(arithmetic_mean(45,32,89,78))
print(arithmetic_mean(8989.8,78787.78,3453,78778.73))
print(arithmetic_mean(45,32))
print(arithmetic_mean(45))
print(arithmetic_mean())

```


---