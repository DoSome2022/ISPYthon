[來源](https://www.w3cschool.cn/python3/)  

## Python3 條件控制  

if語句
Python條件語句是通過一條或多條語句的執行結果(True或者False)來決定執行的代碼塊

<img src="https://atts.w3cschool.cn/attachments/image/20211101/1635732109606721.jpeg">  

Python 中if 語句的一般形式如下所示：  
```
if condition_1:
    statement_block_1
```  
流程圖如下所示：
<img src="https://atts.w3cschool.cn/attachments/image/20211101/1635733665414387.jpeg">  

這種if語句只有在符合條件的時候才會執行代碼塊內的代碼，是一種比較常見的用法。

另一種常見的用法是：
```
if condition_1:
    statement_block_1
else:
    statement_block_2
```  
流程圖如下所示：

<img src="https://atts.w3cschool.cn/attachments/image/20211101/1635733860557125.jpeg">  

這種語句是一種常用的if-else語句，通常用於二分支結構的條件語句代碼。

在一些時候，我們可能需要多分支的條件語句代碼，可以在if-else語句中混合elif語句進行使用：
```
Python 中用elif 代替了else if，所以if語句的關鍵字為：if – elif – else。
```
```
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3

```
流程圖如下所示：
<img src="https://atts.w3cschool.cn/attachments/image/20211101/1635747703593365.jpeg">  
如果"condition_1" 為True 將執行"statement_block_1" 塊語句，如果"condition_1" 為False，將判斷"condition_2"，如果"condition_2" 為True 將執行"statement_block_2" 塊語句，如果"condition_2" 為False，將執行"statement_block_3"塊語句。
```
使用第一種常用的if語句搭配合適的條件可以實現第二種和第三種語句的全部效果，但在執行效率和代碼可讀性上會變得比較糟糕。
```  
注意：  

- 每個條件後面要使用冒號（:），表示接下來是滿足條件後要執行的語句塊。  
- 使用縮進來劃分語句塊，相同縮進數的語句在一起組成一個語句塊。  
- 在Python 中沒有switch – case 語句，但在python3.10中添加了用法類似的match-case語句。  

---  

##  match-case語句（python3.10新特性）  

在其他語言（比如說經典的C語言）中有一種多分支條件判斷語句，可以進行模式匹配（通俗的講，就是將傳入的內容跟多個已存在的樣例進行比較，找到相同的案例並按照該案例的代碼進行處理，如果沒有相同案例就按默認案例進行處理，可以查看其他編程語言的條件語句的Switch相關部分內容進行比較參考）。在python3.10中也引入了這樣的新特性。

一個match語句的使用示例：
```
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the Internet"

```
上述代碼等價於：
```
def http_error(status):
    if status == 400:
        return "Bad request"
    elif status == 404:
        return "Not found"
    elif status == 418:
        return "I'm a teapot"
    else:
        return "Something's wrong with the Internet"
```

---
以下為if 中常用的操作運算符:
![Alt text](image.png)
  
實例  
```
print(5 == 6)
# 使用變量
x = 5
y = 8
print(x == y)

```

```

number = 7
guess = -1
print("猜數字!")
while guess != number:
    guess = int(input("請輸入你要猜的數字"))
    if guess == number:
        print("你猜中了，真厲害！")
    elif guess < number:
        print("猜小了，再猜猜？")
    elif guess > number:
        print("猜大了，在猜猜？")
```
(index.py)

---