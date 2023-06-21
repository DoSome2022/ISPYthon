print(5 == 6)
# 使用變量
x = 5
y = 8
print(x == y)

#--- 練習
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