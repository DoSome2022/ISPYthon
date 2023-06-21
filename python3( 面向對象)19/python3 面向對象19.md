[來源](https://www.w3cschool.cn/python3/)  

## Python3 面向對象
Python 從設計之初就是一門面向對象的語言，正因為如此，在Python 中創建一個類和對像是很容易的。
簡單的了解下面向對象的一些基本特徵。

---
## Python3 面向對象技術簡介

- 類(Class): 用來描述具有相同的屬性和方法的對象的集合。它定義了該集合中每個對象所共有的屬性和方法。對像是類的實例。  
- 類變量：類變量在整個實例化的對像中是公用的。類變量定義在類中且在函數體之外。類變量通常不作為實例變量使用。  
- 數據成員：類變量或者實例變量用於處理類及其實例對象的相關的數據。  
- 方法重寫：如果從父類繼承的方法不能滿足子類的需求，可以對其進行改寫，這個過程叫方法的覆蓋（override），也稱為方法的重寫。  
- 局部變量：定義在方法中的變量，只作用於當前實例的類。  
- 實例變量：在類的聲明中，屬性是用變量來表示的。這種變量就稱為實例變量，是在類聲明的內部但是在類的其他成員方法之外聲明的。  
- 繼承：即一個派生類（derived class）繼承基類（base class）的字段和方法。繼承也允許把一個派生類的對像作為一個基類對像對待。例如，有這樣一個設計：一個Dog 類型的對象派生自Animal 類，這是模擬"是一個（is-a）"關係（例圖，Dog 是一個Animal）。  
- 實例化：創建一個類的實例，類的具體對象。  
- 方法：類中定義的函數。  
- 對象：通過類定義的數據結構實例。對象包括兩個數據成員（類變量和實例變量）和方法。  

---

## 類定義

```
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>

```
類實例化後，可以使用其屬性，實際上，創建一個類之後，可以通過類名訪問其屬性。

---

## 類對象

類對象支持兩種操作：屬性引用和實例化。

屬性引用使用和Python 中所有的屬性引用一樣的標準語法：obj.name。

類對象創建後，類命名空間中所有的命名都是有效屬性名。所以如果類定義是這樣:

```
class MyClass:
    """一個簡單的類實例"""
    i = 12345
    def f(self):
        return 'hello world'

# 實例化類
x = MyClass()

# 訪問類的屬性和方法
print("MyClass 類的屬性 i 為：", x.i)
print("MyClass 類的方法 f 輸出為：", x.f())

```
實例化類：
```
# 實例化類
x = MyClass()
# 訪問類的屬性和方法
```
以上創建了一個新的類實例並將該對象賦給局部變量x，x 為空的對象。  
執行以上程序輸出結果為：
```
MyClass 類的屬性 i 為： 12345
MyClass 類的方法 f 輸出為： hello world
```

---

很多類都傾向於將對象創建為有初始狀態的。因此類可能會定義一個名為__init__() 的特殊方法（構造方法），像下面這樣：  

```
def __init__(self):
    self.data = []
```

---

## 繼承  
Python 同樣支持類的繼承，如果一種語言不支持繼承，類就沒有什麼意義。派生類的定義如下所示:  
```
class DerivedClassName(BaseClassName1):
    <statement-1>
    .
    .
    .
    <statement-N>
```
需要注意圓括號中基類的順序，若是基類中有相同的方法名，而在子類使用時未指定，Python 從左至右搜索即方法在子類中未找到時，從左到右查找基類中是否包含方法。  
BaseClassName（示例中的基類名）必須與派生類定義在一個作用域內。除了類，還可以用表達式，基類定義在另一個模塊中時這一點非常有用:
```
class DerivedClassName(modname.BaseClassName):
```
實例
```
#類定義
class people:
    #定義基本屬性
    name = ''
    age = 0
    #定義私有屬性,私有屬性在類外部無法直接進行訪問
    __weight = 0
    #定義構造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 說: 我 %d 歲。" %(self.name,self.age))

#單繼承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #調用父類的構函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆寫父類的方法
    def speak(self):
        print("%s 說: 我 %d 歲了，我在讀 %d 年級"%(self.name,self.age,self.grade))



s = student('ken',10,60,3)
s.speak()
```

---


##  多繼承

Python 同樣有限的支持多繼承形式。多繼承的類定義形如下例:

```
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

需要注意圓括號中父類的順序，若是父類中有相同的方法名，而在子類使用時未指定，Python 從左至右搜索即方法在子類中未找到時，從左到右查找父類中是否包含方法。  
```
#類定義
class people:
    #定義基本屬性
    name = ''
    age = 0
    #定義私有屬性,私有屬性在類外部無法直接進行訪問
    __weight = 0
    #定義構造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 說: 我 %d 歲。" %(self.name,self.age))

#單繼承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #調用父類的構函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆寫父類的方法
    def speak(self):
        print("%s 說: 我 %d 歲了，我在讀 %d 年級"%(self.name,self.age,self.grade))

#另一個類，多重繼承之前的準備
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一個演說家，我演講的主題是 %s"%(self.name,self.topic))

#多重繼承
class sample(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample("Tim",25,80,4,"Python")
test.speak()   #方法名同，默認調用的是在括號中排前地父類的方法
```

---

## 方法重寫  
如果你的父類方法的功能不能滿足你的需求，你可以在子類重寫你父類的方法，實例如下：

```
class Parent:        # 定義父類
   def myMethod(self):
      print ('調用父類方法')

class Child(Parent): # 定義子類
   def myMethod(self):
      print ('調用子類方法')

c = Child()          # 子類實例
c.myMethod()         # 子類調用重寫方法
```
---

##  類的專有方法：  

- __ init __ : 構造函數，在生成對象時調用  
- __ del __ : 析構函數，釋放對象時使用  
- __ repr __ : 打印，轉換  
- __ setitem __ : 按照索引賦值  
- __ getitem __: 按照索引獲取值  
- __ len __: 獲得長度  
- __ cmp __: 比較運算  
- __ call __: 函數調用  
- __ add __: 加運算    
- __ sub __: 減運算  
- __ mul __: 乘運算  
- __ div __: 除運算  
- __ mod __: 求餘運算  
- __ pow __: 乘方  

----