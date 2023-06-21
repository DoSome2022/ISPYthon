[來源](https://www.w3cschool.cn/python3/)  
## Python3 集合  

集合（set）是一個無序的不重複元素序列。因此在每次運行的時候集合的運行結果的內容都是相同的，但元素的排列順序卻不是固定的，所以本章中部分案例的運行結果會出現與給出結果不同的情況（運行結果不唯一）。

可以使用大括號 { } 或者 set() 函數創建集合，注意：創建一個空集合必須用 set() 而不是 { }，因為 { } 是用來創建一個空字典。

創建格式：  
```
parame = {value01,value02,...}
或者
set(value)
```
集合實例：  
```
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 這裡演示的是去重功能

print('orange' in basket)                 # 快速判斷元素是否在集合內
print('crabgrass' in basket)
```  
運行結果：  
```
{'pear', 'banana', 'orange', 'apple'}
True
False
```
集合的運算：  
```
a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)

print(a-b)

print(a|b)

print(a&b)

print(a^b)
```  
運行結果：  
```
{'b', 'd', 'a', 'c', 'r'}
{'l', 'z', 'm', 'a', 'c'}
{'r', 'd', 'b'}
{'l', 'z', 'b', 'm', 'd', 'a', 'c', 'r'}
{'c', 'a'}
{'l', 'z', 'b', 'm', 'r', 'd'}
```

--- 

## 集合的基本操作  

1、添加元素
語法格式如下：
```
s.add( x )
```
將元素x 添加到集合s 中，如果元素已存在，則不進行任何操作。
```
thisset = set(("s","ss","sss"))
thisset.add("ssss")

print(thisset)
```
運行結果：
```
{'s', 'ss', 'ssss', 'sss'}
```  
還有一個方法，也可以添加元素，且參數可以是列表，元組，字典等，語法格式如下：
```
s.update( x )
```  
x 可以有多個，用逗號分開。  
實例：
```
thisset = set(("s","ss","sss"))
thisset.update({'s1',1})
print(thisset)
thisset.update([11,1],["s1","s2"])
print(thisset)
```

---  
## 移除元素  

語法格式如下：  
```
s.remove( x )
```
將元素x 從集合s 中移除，如果元素不存在，則會發生錯誤。

實例：
```
thisset = set(("s","ss","sss"))
thisset.remove('sss')
print(thisset)
```
用remove() 如果元素不存在,會發生錯誤  
用discard() 如果元素不存在,不會發生錯誤 

隨機刪除集合中的一個元素，語法格式如下:
```
s.pop() 
```
實例：
```
thisset = set(("s","ss","sss"))
```
輸出結果：
```
1.
s
{'sss', 'ss'}
2.
sss
{'s', 'ss'}
3.
ss
{'sss', 's'}
4.
ss
{'sss', 's'}
```
結果每次都不同  

set 集合的pop 方法會對集合進行無序的排列，然後將這個無序排列集合的左面第一個元素進行刪除。因為這個過程是不確定的，所以刪除結果也是不確定的，不建議使用這種方式進行刪除。  

---  

## 計算集合元素個數  
語法格式如下：
```
len(s)
```
計算集合s 的元素個數。

實例：
```
thisset = set(("s","ss","sss"))
print(len(thisset))
```  
運行結果：  
```
3
```

## 清空集合  
語法格式如下：
```
s.clear()
```  
清空集合s。

實例 :
```
thisset = set(("s","ss","sss"))
thisset.clear()
print(thisset)
```
運行結果：  
```
set()
```
## 判斷元素是否在集合中存在  
語法格式如下：
```
x in s
```  
判斷元素x 是否在集合s 中，存在則返回True，不存在則返回False。

實例：  
```
thisset = set(("s","ss","sss"))
print("ss" in thisset )
print("sssss" in thisset )
```
運行結果：  
```
True
False
```

---