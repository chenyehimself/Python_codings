#Homework_01
print("homework 1")
N = 4
ListN =[4,3,2,1]
n = 0
for i in range(N-1):
    for j in range(N-i-1):
        if ListN[j] > ListN[j+1]:
            ListN[j], ListN[j+1] = ListN[j+1], ListN[j]
            n += 1
        elif ListN[j]<=ListN[j+1]:
            n += 0
print(n)
print("\n")
#Homework_02
print("homework 2")
N2 = 4
print(N2)
List2 = []#创建一个空列表获取初始数据组
for i in range(N2):
    List2.append(0)
def reverse(a):
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = 1
        elif a[i] == 1:
            a[i] = 0
for i in range(N2):
    reverse(List2)
    if List2[i]==0:
        List2[i]=1
    elif List2[i]==1:
        List2[i]=0
    for i in List2:
        print(i, sep="", end="")
    print("")
print("\n")
#Homework_03
print("homework 3")
m = 0 #烟蒂
n = 4
k = 3
n = 10
k = 3
result = 0
result = n#对变量的重新赋值
if n>=k:
    result = (n + (n - 1) //(k - 1))
print(result)
#一共抽的烟和拥有过的烟蒂的数量一定，多抽烟的方程化简，最后换来的一根烟是没办法换的，所以烟蒂的数量要-1























