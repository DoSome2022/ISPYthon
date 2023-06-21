[來源](https://www.w3cschool.cn/python3/)

## Python3 字典

在Python3中字典（dictionary ，簡寫為dict）是另一種可變容器模型，且可存儲任意類型對象。

字典的每個鍵值(​ key=>value​) 對用冒號( : ) 分割，每個對之間用逗號( , ) 分割，整個字典包括在花括號(​ {}​) 中,格式如下所示：

```
dict = {key1 : value1, key2 : value2 }
```
鍵必須是唯一的，但值則不必(上表中Danna和Alice的鍵是不同的，值卻是相同的)。

值可以取任何數據類型，但​鍵必須是不可變的​，如字符串，數字或元組。

一個簡單的字典實例：
```
dict={'China':'CN' , 'Hong Kong':'HK ', 'Taiwan':'TW' }
```
也可如此創建字典：
```
dict1= {'	
China':86}

dict2 = {'Hong Kong':22.30858031775129, 114.16673551288073}
```
---

## 訪問字典裡的值
與列表取值類似，但列表取值時使用索引，字典取值時使用key，如下實例:  

```
dict = {'Country': 'China' , 'abbreviation' : 'CN' , 'code' : '86'}

print("dict[Country]: ",dict['Country'])
print("dict[code]: ",dict['code'])

```
以上實例輸出結果：
```
dict[Country]:  China
dict[code]:  86
```
(index.py)

---  
##  修改字典  
向字典添加新內容的方法是增加新的鍵/值對，修改或刪除已有鍵/值對如下實例:  
```
dict = {'Country': 'China' , 'abbreviation' : 'CN' , 'code' : '86'}

dict['Country'] = 'Hong Kong'
dict['abbreviation'] = "HK"
dict['code'] = 852

print("dict[Country]: ",dict['Country'])
print("dict['abbreviation']: ",dict['abbreviation'])
print("dict[code]: ",dict['code'])

```
以上實例輸出結果：
```
dict[Country]:  Hong Kong
dict['abbreviation']:  HK
dict[code]:  852
```
(index.py)

--- 

## 字典鍵的特性  
字典值可以沒有限制地取任何Python 對象，既可以是標準的對象，也可以是用戶定義的，但鍵不行。

兩個重要的點需要記住：

1）不允許同一個鍵出現兩次。創建時如果同一個鍵被賦值兩次，後一個值會被記住，如下實例：
```
dict = {'Country': 'China' , 'abbreviation' : 'CN' , 'code' : '86',  'Country': 'Taiwan' }

print("dict[Country]: ",dict['Country'])
```
以上實例輸出結果：
```
dict[Country]:  Taiwan
```
2）鍵必須不可變，所以可以用數字，字符串或元組充當，而用列表就不行，如下實例：

```
dict = {['Country']: 'China' , 'abbreviation' : 'CN' , 'code' : 86}

print("dict['Country']: ",dict['Country'])
```
以上實例輸出結果：
```
Traceback (most recent call last):
...\index.py", line 23, in <module>     
    dict = {['Country']: 'China' , 'abbreviation' : 'CN' , 'code' : 86}
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'
```
(index.py)

---
## 字典內置函數&方法  
Python 字典包含了以下內置函數：  
- len() 計算字典元素個數，即鍵的總數。
```
dict = {'Country': 'China' , 'abbreviation' : 'CN' , 'code' : 86}

print(len(dict))
```

- str() 以字符串的形式輸出字典（字符串可打印，字典不可打印）。
```
dict = {'Country': 'China' , 'abbreviation' : 'CN' , 'code' : 86}

print(str(dict))
```
- type() 返回輸入的變量類型，如果變量是字典就返回字典類型。
```
dict = {'Country': 'China' , 'abbreviation' : 'CN' , 'code' : 86}

print(type(dict))
```
(index.py)

---