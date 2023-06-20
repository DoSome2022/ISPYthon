dic = {}  # 創建空字典
tel = {'Jack':1557, 'Tom':1320, 'Rose':1886}
print(tel)
print(tel['Jack'])   # 主要的操作：通過key查詢
del tel['Rose']  # 刪除一個鍵值對
tel['Mary'] = 4127  # 添加一個鍵值對
print(tel)

list(tel.keys())  # 返回所有key組成的list

sorted(tel.keys()) # 按key排序