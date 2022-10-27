#Homework_p1179
a,b=map(int,input().split())
sum = 0
list = []
print("list 1")
for i in range(b-a+1):
    c = a
    c = str(c)
    c = str(c)
    for i in range(len(str(c))):
        list.append(int(c[i]))
    a += 1
for i in list:
    if i == 2:
        sum += 1
print(sum)
print("\n")

#Homework_1317
#这个input不太会写...
n=int(10)
List=[0,1,0,2,1,2,0,0,2,0]
m = -1
if List[0]>=List[1]:
    m = 0
for i in range(n-2):
    if List[i+1] > List[i] and List[i+1] >= List[i+2]:
        m += 1
    elif List[i+1] > List[i+2] and List[i+1] >= List[i]:
        m += 1
print(m)
print("\n")

#Homework_1321
boy=0
girl=0
str1 = "......boyogirlyy......girl......."
for i in range(len(str1)):
    if str1[i]=='b' and str1[i+1]=='o' and str1[i+2]=='y':
        boy += 1
    if str1[i]=='g' and str1[i+1]=='i' and str1[i+2]=='r' and str1[i+3]=='l':
        girl += 1
print(boy)
print(girl)
print("\n")
#我题目没看懂...