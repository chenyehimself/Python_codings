#Homework_01
print("Homework_01")
n = int(input("Enter input: "))
for i in range(2,n+1):
    if n%i == 0:
        print(int(n/i))
        break
print("\n")
#错了 去看老师答案
#没错 是我脑子抽了
#Homework_02
print("Homework_02")
'''
a1 = int(input("1sta:")); a2 = int(input("1stb:"))
b1 = int(input("2nda:")); b2 = int(input("2ndb:"))
c1 = int(input("3rda:")); c2 = int(input("3rdb:"))
d1 = int(input("4tha:")); d2 = int(input("4thb:"))
e1 = int(input("5tha:")); e2 = int(input("5thb:"))
f1 = int(input("6tha:")); f2 = int(input("6thb:"))
g1 = int(input("7tha:")); g2 = int(input("7thb:"))'''
a1 = 5 ; a2 = 3
b1 = 6 ; b2 = 2
c1 = 7 ; c2 = 2
d1 = 5 ; d2 = 3
e1 = 5 ; e2 = 4
f1 = 0 ; f2 = 4
g1 = 0 ; g2 = 6
#sum up:
a = a1 + a2
b = b1 + b2
c = c1 + c2
d = d1 + d2
e = e1 + e2
f = f1 + f2
g = g1 + g2
list1 = [a,b,c,d,e,f,g]
gate1 = 0
list2 = []#创建一个空列表
for i in range(7):
    if list1[i] > 8:
        gate1 += 1
if gate1 == 0:
    print(0)
else:
    for i in range(7):
        if int(list1[i]) > 8:
            list2.append(list1[i])
    for i in range(7):
        if int(max(list2)) == int(list1[i]):
            print(i+1)
            break
print("\n")
#Homework_03
print("Homework_03")
#Test_1
print("Test_1")
c1 = 290
c2 = 230
c3 = 280
c4 = 200
c5 = 300
c6 = 170
c7 = 340
c8 = 50
c9 = 90
c10 = 80
c11 = 200
c12 = 60
m = 0
s = 0
C = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12]
gate2 = 1
#如果gate2=0那么死亡 游戏结束
#思维草稿：每个月月初m+300开始循环，先判断预算够不够 不够直接死
# 然后【判断】减去budget看是否大于等于100
#如果小于一百，跳入下一个判断
#如果大于等于一百，对m-c的值进行一百整除提取商（%）,加入saving中，并将（m-c）模100的值输入m
#如果小于一百，pass m+300-c的值，覆盖掉手头的钱m进入第二月
#如果上个月pass下来的m值加上300减去预算小于0，循环停止将该月份返回打印出来
for i in range(12):
    m += 300
    if m - int(C[i]) < 0:
        gate2 = 0
        print(-(i+1))
        break
    elif m - int(C[i]) < 100:
        m = m - int(C[i])
    elif m - int(C[i]) >= 100:
        s += ((m - int(C[i]))//100)
        m = (m - int(C[i]))%100
if gate2 == 1:
    print( s*120 +m )

#Test_2
print("Test_2")
c1 = 290
c2 = 230
c3 = 280
c4 = 200
c5 = 300
c6 = 170
c7 = 330
c8 = 50
c9 = 90
c10 = 80
c11 = 200
c12 = 60

m = 0
s = 0
C = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12]
gate2 = 1
for i in range(12):
    m += 300
    if m - int(C[i]) < 0:
        gate2 = 0
        print(-(i+1))
        break
    elif m - int(C[i]) < 100:
        m = m - int(C[i])
    elif m - int(C[i]) >= 100:
        s += ((m - int(C[i]))//100)
        m = (m - int(C[i]))%100
if gate2  == 1:
    print(s*120+m)
    print("The calculation has finished.")











