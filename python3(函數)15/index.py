#--- 

def hello():
    print("hello World!")

hello()

#---

def area(width, height):
    return width * height
 
def print_welcome(name):
    print("Welcome", name)

print_welcome("Fred")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

#---

a = 4  # 全局變量
 
def print_func1():
    a = 17 # 局部變量
    print("in print_func a = ", a)


def print_func2():   
    print("in print_func a = ", a)


print_func1()
print_func2()
print("a = ", a)

#--- return

def return_sum(x,y):
    c = x + y
    return c


res = return_sum(4,5)
print(res)

#--- 可變參數列表

def arithmetic_mean(*args):
    if len(args) == 0:
        return 0
    else:
        sum = 0
        for x in args:
            sum += x
        return sum/len(args)


print(arithmetic_mean(45,32,89,78))
print(arithmetic_mean(8989.8,78787.78,3453,78778.73))
print(arithmetic_mean(45,32))
print(arithmetic_mean(45))
print(arithmetic_mean())

