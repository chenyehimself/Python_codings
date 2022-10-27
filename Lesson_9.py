n = int(input())
long_list=[]
listX = []
listY = []

for i in range(n):
    a,b = map(int,input().split())
    tmp_list = [a,b]
    long_list.append(tmp_list)

for i in range(n):
    listX.append(long_list[i][0])
    listY.append(long_list[i][1])

listXsorted = []
listYsorted = []

for i in range(n):
    listx = listX.copy()
    del listx[i]
    listXsorted.append(listx)

for i in range(n):
    listy = listY.copy()
    del listy[i]
    listYsorted.append(listy)
listproduct = []#创建空列表列出所有乘积
for i in range(n):
    listproduct.append((max(listXsorted[i])-1)*(max(listYsorted[i])-1))
print(min(listproduct))










