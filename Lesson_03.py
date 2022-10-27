#Classnotes&Exercices
str1 = "Hello, world!"
print(str1[4])
print(str1[:])#：衔接开始和结束，包头不包尾
print(str1[3:])
print(str1[3:10])
print(str1[:10])
print(str1[-3])
print("\n")
#string不可更改其中的内容
#str[0] = "J"
str1 = "Jello, world!"#method_01
print(str1)
str1 = "J" + str1[1:]
print(str1)
#Classwork_02
prefixes = "JKLMNOPQ"
suffix = "ack"
for c in prefixes:
    print(c + suffix)
print("\n")
for i in range(len(prefixes)):
    print(prefixes[i] + suffix)
#Classwork_03
def find(str,ch):
    for i in range(len(str)):
        if ch == str[i]:
            return(i)
            break
        else:
            return("-1")
print(find("Compsci","p"))
print("\n")

#Classwork_04
def dis(point1,point2):
    #[1,1], [2,2]
    list1 = point1
    list2 = point2
    print( ( (list1[0]-list2[0])**2 + (list1[1]-list2[1])**2)**0.5)
dis([1,1], [3,3])
print("\n")
#==================我是分界线===================
#从这里开始是课后作业
#思考题2
martrice = [[1,2,3],[4,5,6],[7,8,9]]
print(martrice[0])
'''mar = [1,2,3]
sum = 0
for i in mar:
    sum = i + sum
print(sum)'''
print("method 1")
total = 0
for c in martrice:
    sum1 = 0
    for i in martrice[0]:
        sum1 = i + sum1
    sum2 = 0
    for i in martrice[1]:
        sum2 = i +sum2
    sum3 = 0
    for i in martrice[2]:
        sum3 = i + sum3
total = sum1 + sum2 + sum3
print(total)
print("method 2")
sum = 0
for a in range(3):
    for b in range(3):
        sum = sum + martrice[a][b]
print(sum)
print("\n")

'''sum1 = 0
for i in martrice[0]:
    sum1 = i + sum1
print(sum1)
'''
#洛谷Homework_01
print("Please enter ten sets of values below for the heights from apples to the eground(unit:cm).Values can vary from 100cm to 200cm.")
a0 = int(input("Height1:"))
a1 = int(input("Height2:"))
a2 = int(input("Height3:"))
a3 = int(input("Height4:"))
a4 = int(input("Height5:"))
a5 = int(input("Height6:"))
a6 = int(input("Height7:"))
a7 = int(input("Height8:"))
a8 = int(input("Height9:"))
a9 = int(input("Height10:"))
List1 = [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]
h = int(input("Please enter the maximum height that the person can reach(h from 110 to 120cm): "))
print("Your list is : ")
print(List1)
print("your value for h is: ")
print(h)
result = 0
progress = 0
value_h = 0
value_as = 0
for i in List1:
    if i <= 200 and i >= 100:
        pass
        progress = 1
        value_as = 1
        if h <= 120 and h >= 110:
            pass
            progress = 1
            value_h = 1
            for i in range(10):
                if (h + 30) >= List1[i]:
                    result += 1
        else:
            progress = 0
            value_h = 0
            break
    else:
        progress = 0
        value_as = 0
        break

if result >= 0 and progress == 1:
    print("Final output is : ")
    print(int(result/10))

if value_as == 0 :
    print("invalid input for heights of apples.")

if value_h == 0 :
    print("invalid input for h.")
print("\n")
#洛谷Homework_02 不太知道输入格式怎么做...😭但是知道思路：将所有树木都标为1，区域里的标为0 最后数有多少个0
'''
L = input("Please enter the length of the road(0<L<10000): ")
'''
#洛谷Homework_03
import random
N = random.randint(0,100)
print("Input: ")
print(N)
List3 = []
for i in range(N):
    List3.append(random.randint(0,1000))
print(List3)
List31 = sorted(List3)
result = 0
for n in range(N):
    if List31[n] != List31[n-1]:
        result += 1
print("Output:")
print(result)
print(List31)



























