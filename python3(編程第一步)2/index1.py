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