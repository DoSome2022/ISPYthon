[來源](https://www.w3cschool.cn/python3/)  

## Python3 錯誤和異常

作為Python 初學者，在剛學習Python 編程時，經常會看到一些報錯信息
Python 有兩種錯誤很容易辨認：語法錯誤和異常。

## 語法錯誤
Python 的語法錯誤或者稱之為解析錯，是初學者經常碰到的，如下實例
```
 while True print('Hello world')
  File "<stdin>", line 1, in ?
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

這個例子中，函數print() 被檢查到有錯誤，是它前面缺少了一個冒號（:）。

語法分析器指出了出錯的一行，並且在最先找到的錯誤的位置標記了一個小小的箭頭。


## 異常
即便Python 程序的語法是正確的，在運行它的時候，也有可能發生錯誤。運行期檢測到的錯誤被稱為異常。

大多數的異常都不會被程序處理，都以錯誤信息的形式展現在這裡:
```
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: Can't convert 'int' object to str implicitly
```

異常以不同的類型出現，這些類型都作為信息的一部分打印出來: 例子中的類型有ZeroDivisionError，NameError 和TypeError。

錯誤信息的前面部分顯示了異常發生的上下文，並以調用棧的形式顯示具體信息。

---
