str = "python"
print(str[0],"==",str[-6])
print(str[5],"==",str[-1])

# str = "python"
 #取索引區間為[0,2]之間（不包括索引2處的字符）的字符串
# print(str[:2])
 #隔 1 個字符取一個字符，區間是整個字符串
# print(str[::2])
 #取整個字符串，此時 [] 中只需一個冒號即可
# print(str[:])  

# str1 = "py"
# str2 = "th"
# str3 = "on"

# print(" : ",str1+str2+str3)


str4 = "python-django"
#找出最大的字符
print(max(str4))
#找出最小的字符
print(min(str4))
#對字符串中的元素進行排序
print(sorted(str4))