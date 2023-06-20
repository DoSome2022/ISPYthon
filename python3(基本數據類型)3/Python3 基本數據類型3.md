[來源](https://www.w3cschool.cn/python3/)  
## Python3 基本數據類型
---
在Python 中，變量就是變量，它沒有類型，我們所說的"類型"是變量所指的內存中對象的類型。
Python 3 中有六個標準的數據類型：  

- Numbers（數字）
- String（字符串）
- List（列表）
- Tuple（元組）
- Sets（集合）
- Dictionaries（字典）
---
## Numbers（數字）  
Python 3 支持int（整型）、float（浮點型）、bool（布爾型）、complex（複數）。

數值類型的賦值和計算都是很直觀的，就像大多數語言一樣。內置的type() 函數可以用來查詢變量所指的對像類型。
```
 a, b, c, d = 20, 5.5, True, 4+3j
 print(type(a), type(b), type(c), type(d))
 <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
```
還可以用isinstance來判斷：
```
aa = 111
print(isinstance(aa,int))

```
isinstance和type的區別在於：    
- type（）不會認為子類是一種父類類型。  
- isinstance（）會認為子類是一種父類類型。  

```
class A:
    pass

class B(A):
    pass
 
print(isinstance(A(), A))
print(type(A()) == A) 
print(isinstance(B(), A))
print(type(B()) == A)

```
當你指定一個值時，Number 對象就會被創建：  
```
var1 = 1
var2 = 10
```
---

1、Python 可以同時為多個變量賦值，如a, b = 1, 2。  
2、一個變量可以通過賦值指向不同類型的對象。  
3、數值的除法（/）總是返回一個浮點數，要獲取整數使用​//​操作符。  
4、在混合計算時，Python 會把整型轉換成為浮點數  

(index.py)

---
## String（字符串） 
Python 中的字符串str 用單引號(' ')或雙引號(" ") 括起來，同時使用反斜杠(\) 轉義特殊字符。
```
s = 'Yes,he doesn\'t'
print(s, type(s), len(s))
```
如果你不想讓反斜杠發生轉義，可以在字符串前面添加一個r，表示原始字符串：
```
print('C:\some\name')

print(r'C:\some\name')

```
字符串可以使用+ 運算符串連接在一起，或者用* 運算符重複：
```
print('str'+'ing', 'my'*3)
```  
Python 中的字符串有兩種索引方式，  
第一種是從左往右，從0 開始依次增加；  
第二種是從右往左，從-1 開始依次減少。

注意，沒有單獨的字符類型，一個字符就是長度為1 的字符串。
```
word = 'Python'
print(word[0], word[5])

print(word[-1], word[-6])
```  
還可以對字符串進行切片，獲取一段子串。用冒號分隔兩個索引，形式為變量[頭下標:尾下標]。

截取的範圍是前閉後開的（頭下標取，尾下標不取），並且兩個索引都可以省略：
```
word = 'ilovepython'
word[1:5]
word[:]
word[5:]
word[-10:-6]
```  
與C 字符串不同的是，Python 字符串不能被改變。向一個索引位置賦值，比如word[0] = 'm' 會導致錯誤。  
注意：  

1、反斜杠可以用來轉義，使用r 可以讓反斜杠不發生轉義。  
2、字符串可以用+ 運算符連接在一起，用* 運算符重複。  
3、Python 中的字符串有兩種索引方式，從左往右以0 開始，從右往左以-1 開始。  
4、Python 中的字符串不能改變。  


(index1.py)

---  
## List（列表）

List（列表） 是Python 中使用最頻繁的數據類型。

列表是寫在方括號之間、用逗號分隔開的元素列表。列表中元素的類型可以不相同：

```
a = ['him', 25, 100, 'her']
print(a)
```
和字符串一樣，列表同樣可以被索引和切片，列表被切片後返回一個包含所需元素的新列表。詳細的在這裡就不贅述了。

列表還支持串聯操作，使用+ 操作符：

```
a = [1, 2, 3, 4, 5]
a + [6, 7, 8]
```
與Python 字符串不一樣的是，列表中的元素是可以改變的：
```
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
a

a[2:5] = []   # 删除
a

```
List 內置了有很多方法，例如append()、pop() 等等，這在後面會講到。

注意：  

1、List 寫在方括號之間，元素用逗號隔開。  
2、和字符串一樣，List 可以被索引和切片。  
3、List 可以使用+ 操作符進行拼接。  
4、List 中的元素是可以改變的。  

(index2.py)

---
## Tuple（元組）  
元組（tuple）與列表類似，不同之處在於元組的元素不能修改。元組寫在小括號裡，元素之間用逗號隔開。  
元組中的元素類型也可以不相同：
```
a = (1991, 2014, 'physics', 'math')
print(a, type(a), len(a))
```
元組與字符串類似，可以被索引且下標索引從0 開始，也可以進行截取/切片（看上面，這裡不再贅述）。

其實，可以把字符串看作一種特殊的元組。
```
tup = (1, 2, 3, 4, 5, 6)
print(tup[0], tup[1:5])

tup[0] = 11  # 修改元组元素的操作是非法的
```  
雖然tuple 的元素不可改變，但它可以包含可變的對象，比如list 列表。

構造包含0 個或1 個元素的tuple 是個特殊的問題，所以有一些額外的語法規則
```
tup1 = () # 空元组
tup2 = (20,) # 一個元素，需要在元素後添加逗號
```
另外，元組也支持用+ 操作符：
```
tup1, tup2 = (1, 2, 3), (4, 5, 6)
print(tup1+tup2)
```  
string、list 和tuple 都屬於sequence（序列）。

注意：

1、與字符串一樣，元組的元素不能修改。  
2、元組也可以被索引和切片，方法都是一樣的。  
3、注意構造包含0 或1 個元素的元組的特殊語法規則。  
4、元組也可以使用+ 操作符進行拼接。  

(index3.py)

---
## Sets（集合）

集合（set）是一個無序不重複元素的集。

基本功能是進行成員關係測試和消除重複元素。

可以使用大括號或者set() 函數創建set 集合，注意：創建一個空集合必須用set() 而不是{ }，因為{ }是用來創建一個空字典。

```
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a和b的差集
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素

```
(index4.py)  

---
## Dictionaries（字典）  
字典（dictionary）是Python 中另一個非常有用的內置數據類型。

字典是一種映射類型（mapping type），它是一個無序的鍵值對（key-value）集合。

關鍵字（key）必須使用不可變類型，也就是說list和包含可變類型的tuple 不能做關鍵字。

在同一個字典中，關鍵字（key）必須互不相同。
```
dic = {}  # 創建空字典
tel = {'Jack':1557, 'Tom':1320, 'Rose':1886}
print(tel)
print(tel['Jack'])   # 主要的操作：通過key查詢
del tel['Rose']  # 刪除一個鍵值對
tel['Mary'] = 4127  # 添加一個鍵值對
print(tel)

list(tel.keys())  # 返回所有key組成的list

sorted(tel.keys()) # 按key排序

```
另外，字典類型也有一些內置的函數，例如clear()、keys()、values() 等。  

注意：

1、字典是一種映射類型，它的元素是鍵值對。  
2、字典的關鍵字必須為不可變類型，且不能重複。  
3、創建空字典使用{ }。  

(index5.py)

---