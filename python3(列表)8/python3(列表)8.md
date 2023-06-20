[來源](https://www.w3cschool.cn/python3/)  

## Python3 列表

列表（list）也是最常用的Python 數據類型之一，它以一個方括號內包含多個其他數據項（字符串，數字等甚至是另一個列表），數據項間以逗號作為分隔的數據類型。

列表的數據項不需要具有相同的類型。（這點是與其他語言的數組的一個區別）

創建一個列表，只要把逗號分隔的不同的數據項使用方括號括起來即可。如下所示：

```
list1 = ['js','py','css','html']
list2 = ['15','26','50']

print("list1 : ",list1)
print("list2 : ",list2)

```
(index.py)

## 訪問列表中的值
與字符串的索引一樣，列表索引從 0 開始，第二個索引是 1，依此類推。

通過索引列表可以進行截取、組合等操作。   

列表索引的操作：
```
list1 = ['js','py','css','html']
print ("list1的第一項: ", list1[0])
print ("list1的最後一項: ", list1[-1])
```
運行結果：
```
list1的第一項:  js
list1的最後一項:  html
```
(index.py)

---

以下是列表切片的操作：
```
list1 = ['js','py','css','html']
print ("list1的前3項: ", list1[0:3])
print ("list1的2、3項: ", list1[1:3])
```

運行結果：
```
list1的前3項:  ['js', 'py', 'css']  
list1的2、3項:  ['py', 'css']  
```
(index.py)

---

## 更新列表
你可以對列表的數據項進行修改或更新，你也可以使用append() 方法來添加列表項，如下所示：
```
list1 = ['js','py','css','html']
print ("list1的第三個元素為: ", list1[2])
list1[2] = "sass"
print ("list1的第三個元素為: ", list1[2])
list1.append(jsx)
print ("追加列表項後的list1: ", list1)

```
運行結果：
```
list1的第三個元素為:  css
list1的第三個元素為:  sass
追加列表項後的list1:  ['js', 'py', 'sass', 'html', 'jsx']
```
(index.py)

---

##  刪除列表元素

可以使用del 語句來刪除列表的的元素，如下實例：

```
list1 = ['js','py','css','html']
del list1[0]
print ("刪除列表項後的list1: ", list1)
```
運行結果：
```
刪除列表項後的list1:  ['py', 'css', 'html']
```
(index.py)

---