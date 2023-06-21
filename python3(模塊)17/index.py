# import sys

# print('命令行參數如下:')
# for i in sys.argv:
#     print(i)

# print('\n\nPython 路徑為：', sys.path, '\n')


# import support

# support.print_func('okok')

import fibo , sys

# fibo.fib(10)

# print(fibo.fib2(20))

# print(fibo.__name__)


# if __name__ == '__main__':
#     print('程序自身在運行')
# else:
#     print('我來自另一模塊')


#內置的函數 dir() 可以找到模塊內定義的所有名稱。以一個字符串列表的形式返回:

print(dir(fibo))
print(dir(sys))