[來源](https://www.w3cschool.cn/python3/)  

## Python3 編程第一步
---
在下例裡，我們能寫出一個初步的斐波納契數列如下：
```
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

```
(在index.py)  

其中代碼​ a, b = b, a + b​ 的計算方式為先計算右邊的表達式，然後同時賦值給左邊，等價於：
```
n = b
m = a + b
a = n
b = m
```
執行以上程序，輸出結果為：
```
1
1
2
3
5
8
```
這個例子介紹了幾個新特徵。  


第一行包含了一個複合賦值：  
變量a 和b 同時得到新值0 和1。  
最後一行也使用了複合賦值的方法：等價於c = a，a = b，b = b + c。

---
最後嘗試使用if 條件控制  
```
age = int(input("請輸入你家狗狗的年齡: "))
print("")
if age < 0:
	print("請輸入正確的年齡。")
elif age == 1:
	print("相當於 14 歲的人。")
elif age == 2:
	print("相當於 22 歲的人。")
elif age > 2:
	human = 22 + (age -2)*5
	print("對應人類年齡: ", human)
### 退出提示，本地環境下可以使用這樣的退出提示使代碼更易用
input('點擊 enter 鍵退出')
```
(在index1.py)  

---